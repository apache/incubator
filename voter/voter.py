#!/usr/bin/env python

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Purpose: Maintaines a list of currently open and recently closed
         votes on the general@incubator mailing list.

It does so by parsing the mbox files of general@incubator and all
active podling list archives and updates information about votes,
based on tags in from the subject lines, in a SQLite database.

Usage: voter.py <mbox_archive_basedir>

   where mbox_archive_basedir is the root directory of all mailing
   list archives in mbox format; e.g., on minotaur, it's

       ~apmail/public-arch

Status: Alpha
"""

from __future__ import absolute_import

import os, re, sys
import argparse
import collections
import datetime
import email
import email.utils
import gzip
import sqlite3

sys.path.insert(0, os.path.dirname(__file__))
from utility import Issue, SiteStructure, UTC
from podlings import Podling, podling_archives


class MBoxParser(object):
    """
    Parser for mail archives in mbox format.
    Scans the archve for all mails addressed To: or Cc: the Incubator
    general mailing list.
    """

    __general_rx = re.compile(r'general@incubator\.apache\.org')
    MBox = collections.namedtuple('MBox', ('mtime', 'entries'))
    Entry = collections.namedtuple('Entry', ('updated', 'title'))

    @classmethod
    def __append_message(cls, text, mbox):
        if not text:
            return

        message = email.message_from_string(text)

        def decode(header):
            header = message[header]
            if header:
                decoded = email.utils.decode_rfc2231(header)
                try:
                    return email.utils.collapse_rfc2231_value(decoded)
                except:
                    return header
            return None

        to = decode('To')
        cc = decode('Cc')
        date = message['Date']
        subject = decode('Subject')
        if not subject or not date:
            return
        # Make sure the subject does not span multiple lines.
        subject = subject.replace('\n', '')

        if not (to and cls.__general_rx.search(to)
                or cc and cls.__general_rx.search(cc)):
            # The message was not sent to general@incubator
            return

        timestamp = email.utils.mktime_tz(email.utils.parsedate_tz(date))
        updated = datetime.datetime.fromtimestamp(timestamp)
        mbox.entries.append(cls.Entry(updated, subject))

    @classmethod
    def __parse_file(cls, text, mtime):
        mbox = cls.MBox(mtime, [])
        start = 0
        while start < len(text):
            end = text.find('\nFrom ', start)
            if 0 > end:
                end = len(text)
            cls.__append_message(text[start:end], mbox)
            start = end + 1             # Skip the newline
        return mbox

    @classmethod
    def parse(cls, mbox_path, mtime):
        if mbox_path.endswith('.gz'):
            with gzip.open(mbox_path) as mbox_file:
                text = mbox_file.read().replace('\r\n', '\n')
                return cls.__parse_file(text, mtime)
        else:
            with open(mbox_path, 'rt') as mbox_file:
                return cls.__parse_file(mbox_file.read(), mtime)


class VoteUpdater(object):
    """
    TODO: Docstring.
    """
    __subject_rx = re.compile(
        # Skip anything before the first tag
        r'^[^[]*'
        # A [RESULT] or [DISCUSS] or [CANCELLED] tag
        # can come before the [VOTE] tag
        r'(\[((?P<result1>RESULTS?)|DISCUSS|(?P<cancel1>CANCELL?(ED)?))\]\s*)?'
        # The [VOTE] tag is required to start a new vote thread, but
        # not to end it
        r'(?P<vote>\[VOTE\]\s*)?'
        # Handle [VOTE][<tag>] as well, just in case
        r'(\[((?P<result2>RESULTS?)|DISCUSS|(?P<cancel2>CANCELL?(ED)?))\]\s*)?'
        # The rest of the subject line, and strip off trailing whitespace
        r'(?P<subject>.*?)\s*$',
        re.IGNORECASE)

    def __init__(self, mbox_archive_basedir):
        self.mbox_basedir = mbox_archive_basedir
        self.mbox_relpaths = []

        archives, self.issues = podling_archives()

        archives.insert(0, Podling('Incubator', 'incubator.apache.org/general'))

        now = datetime.datetime.utcnow()
        thismonth = datetime.datetime(now.year, now.month, 1)
        if now.month == 1:
            lastmonth = datetime.datetime(now.year - 1, 12, 1)
        else:
            lastmonth = datetime.datetime(now.year, now.month - 1, 1)

        current = thismonth.strftime('%Y%m')
        previous = lastmonth.strftime('%Y%m') + '.gz'

        for archive in archives:
            if not archive.mbox_relpath:
                continue
            basedir = os.path.join(mbox_archive_basedir, archive.mbox_relpath)
            if not os.path.isdir(basedir):
                self.issues.record_warning(
                    archive.name + ' has no archive at ' + basedir)
                continue

            if os.path.isfile(os.path.join(basedir, current)):
                self.mbox_relpaths.append(
                    os.path.join(archive.mbox_relpath, current))
            if os.path.isfile(os.path.join(basedir, previous)):
                self.mbox_relpaths.append(
                    os.path.join(archive.mbox_relpath, previous))

    ParsedVote = collections.namedtuple(
        'ParsedVote',
        ('sortkey', 'updated', 'subject', 'closed', 'cancelled', 'threaded'))

    ParsedMBox = collections.namedtuple('ParsedMBox', ('relpath', 'mtime'))

    def __parse_mbox(self, mbox_path, mtime, votes):
        mbox = MBoxParser.parse(mbox_path, mtime)
        for e in mbox.entries:
            parsed = self.__subject_rx.match(e.title)
            if parsed is None:
                continue

            threaded = parsed.group('vote')
            subject = parsed.group('subject')
            cancelled = int(parsed.group('cancel1') is not None
                            or parsed.group('cancel2') is not None)
            if cancelled or parsed.group('result1') or parsed.group('result2'):
                closed = e.updated
            else:
                closed = None

            if not threaded and not (cancelled or closed):
                # Skip discussions that aren't about votes
                continue

            votes.append(self.ParsedVote(subject.upper(), e.updated,
                                         subject, closed, cancelled,
                                         threaded))

    def record(self, database):
        votes = []
        mboxes = []
        for relpath in self.mbox_relpaths:
            mbox_path = os.path.join(self.mbox_basedir, relpath)
            mtime = os.stat(mbox_path).st_mtime
            if mtime != database.mbox_mtime(relpath):
                mboxes.append((mbox_path, relpath, mtime))

        if not mboxes:
            # Nothing to do
            return

        for mbox_path, relpath, mtime in mboxes:
            self.__parse_mbox(mbox_path, mtime, votes)

        timestamp = max(m for p, r, m in mboxes)
        feed_updated = datetime.datetime.utcfromtimestamp(timestamp)

        database.record_votes(feed_updated,
                              ((database.Vote(subject = v.subject,
                                                updated = v.updated,
                                                closed = v.closed,
                                                cancelled = v.cancelled),
                                v.threaded)
                               for v in sorted(votes)),
                               (self.ParsedMBox(r, m) for p, r, m in mboxes))
        database.record_issues(self.issues.issues)


class VoteDatabase(object):
    """
    TODO: Docstring.
    """

    __schema = """
        CREATE TABLE feedinfo (
          rowid INTEGER NOT NULL PRIMARY KEY,
          updated TEXT NOT NULL,
          CONSTRAINT singleton CHECK (rowid = 1)
        );
        INSERT INTO feedinfo (rowid, updated) VALUES (1, '');

        CREATE TABLE issue (
          rowid INTEGER NOT NULL PRIMARY KEY,
          kind TEXT DEFAULT NULL,
          message TEXT NOT NULL
        );

        CREATE TABLE vote (
          sortkey TEXT NOT NULL PRIMARY KEY,
          subject TEXT NOT NULL,
          noticed TEXT NOT NULL,
          updated TEXT NOT NULL,
          closed TEXT DEFAULT NULL,
          cancelled INTEGER DEFAULT 0
        );
        CREATE INDEX updated_index ON vote(updated DESC);
        CREATE INDEX closed_index ON vote(closed DESC);

        CREATE TABLE mbox (
          relpath TEXT NOT NULL PRIMARY KEY,
          mtime FLOAT NOT NULL
        );
        """

    @classmethod
    def __connect(cls, path):
        con = sqlite3.connect(path, isolation_level = 'IMMEDIATE')
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute("PRAGMA page_size = 4096")
        cursor.execute("PRAGMA temp_store = MEMORY")
        cursor.execute("PRAGMA case_sensitive_like = ON")
        cursor.execute("PRAGMA encoding = 'UTF-8'")
        return con

    @classmethod
    def create(cls, path):
        con = cls.__connect(path)
        cursor = con.cursor()
        cursor.executescript(cls.__schema)
        con.close()


    def __init__(self, path, prune_error_message=None):
        assert os.path.isfile(path)
        self.con = self.__connect(path)
        self.__updated = None
        if not prune_error_message:
            self.__prune_error_message = lambda message: message
        else:
            self.__prune_error_message = prune_error_message

    class __Transaction(object):
        __slots__ = ['__db']
        def __init__(self, database):
            self.__db = database
        def __enter__(self):
            self.__db.con.execute("BEGIN")
            return self.__db
        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type is None:
                self.__db.con.commit()
            else:
                try:
                    self.__db.con.rollback()
                except:
                    pass
            return None

    def transaction(self):
        return self.__Transaction(self)

    def close(self):
        self.con.close()

    @property
    def updated(self):
        if self.__updated is None:
            cursor = self.con.cursor()
            cursor.execute("SELECT updated FROM feedinfo WHERE rowid = 1")
            self.__updated = UTC.timeparse(cursor.fetchone()['updated'])
        return self.__updated

    def mbox_mtime(self, relpath):
        cursor = self.con.cursor()
        cursor.execute("SELECT mtime FROM mbox WHERE relpath = ?", (relpath,))
        row = cursor.fetchone()
        return row and row['mtime'] or None

    def record_mbox(self, relpath, mtime):
        self.con.execute("INSERT OR REPLACE INTO mbox"
                         " (relpath, mtime) VALUES (?, ?)",
                         (relpath, mtime))

    class Vote(object):
        __slots__ = ('sortkey', 'subject',
                     'noticed', 'updated', 'closed', 'cancelled')

        def __init__(self, **kwargs):
            for name in self.__slots__:
                setattr(self, name, kwargs.get(name, None))

        def merge(self, other):
            if self is other:
                return

            assert (type(self) == type(other)
                    and (self.subject is None
                         or other.subject is None
                         or self.subject == other.subject))

            if other.updated > self.updated:
                self.updated = other.updated
            if not self.closed:
                self.closed = other.closed
            if not self.cancelled:
                self.cancelled = other.cancelled

        @classmethod
        def find(cls, con, subject):
            sortkey = subject.upper()
            cursor = con.cursor()
            cursor.execute("SELECT subject, noticed, updated, closed, cancelled"
                           " FROM vote WHERE sortkey = ?", (sortkey,))
            row = cursor.fetchone()
            if row is None:
                return None
            vote = cls(sortkey=sortkey, **row)
            vote.noticed = UTC.timeparse(vote.noticed)
            vote.updated = UTC.timeparse(vote.updated)
            vote.closed = UTC.timeparse(vote.closed)
            return vote

        def insert(self, con):
            assert self.sortkey is None and self.subject is not None
            self.sortkey = self.subject.upper()
            if self.noticed is None:
                self.noticed = self.updated
            con.execute("INSERT INTO vote"
                        " (sortkey, subject, noticed, updated, closed, cancelled)"
                        " VALUES (?, ?, ?, ?, ?, ?)",
                        (self.sortkey, self.subject,
                         UTC.timestring(self.noticed),
                         UTC.timestring(self.updated),
                         UTC.timestring(self.closed),
                         self.cancelled))

        def update(self, con):
            assert self.sortkey is not None
            assert self.subject.upper() == self.sortkey
            con.execute("UPDATE vote SET"
                        " noticed = ?, updated = ?, closed = ?, cancelled = ?"
                        " WHERE sortkey = ?",
                        (UTC.timestring(self.noticed),
                         UTC.timestring(self.updated),
                         UTC.timestring(self.closed),
                         self.cancelled, self.sortkey))

    def record_votes(self, updated, votes, mboxes):
        with self.transaction() as txn:
            for v, threaded in votes:
                vote = txn.Vote.find(txn.con, v.subject)
                if vote:
                    vote.merge(v)
                    vote.update(txn.con)
                elif threaded:
                    v.insert(txn.con)

            for m in mboxes:
                txn.record_mbox(m.relpath, m.mtime)

            txn.con.execute("UPDATE feedinfo SET updated = ?",
                            (UTC.timestring(updated),))
            txn.__updated = None
        pass

    def record_issues(self, issues):
        with self.transaction() as txn:
            cursor = txn.con.cursor()
            cursor.execute("DELETE FROM issue");
            if not issues:
                return
            for kind, message in issues:
                cursor.execute("INSERT INTO issue (kind, message)"
                               " VALUES (?, ?)",
                               (kind, self.__prune_error_message(message)))

    def __list_votes(self, active):
        if active:
            sql = ("SELECT sortkey, subject, noticed, updated, closed, cancelled"
                   " FROM vote WHERE closed IS NULL ORDER BY updated DESC")
        else:
            sql = ("SELECT sortkey, subject, noticed, updated, closed, cancelled"
                   " FROM vote WHERE closed IS NOT NULL ORDER BY closed DESC")
        cursor = self.con.cursor()
        cursor.execute(sql)
        for row in cursor.fetchall():
            vote = self.Vote(**row)
            vote.noticed = UTC.timeparse(vote.noticed)
            vote.updated = UTC.timeparse(vote.updated)
            vote.closed = UTC.timeparse(vote.closed)
            yield vote

    def list_open_votes(self):
        return self.__list_votes(True)

    def list_resolved_votes(self):
        return self.__list_votes(False)

    def list_issues(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT kind, message FROM issue"
                       " ORDER BY rowid ASC")
        for row in cursor.fetchall():
            yield(Issue(**row))

    def prune_old_votes(self):
        now = datetime.datetime.utcnow()
        cursor = self.con.cursor()
        cursor.execute("SELECT sortkey, updated FROM vote"
                       " WHERE closed IS NOT NULL ORDER BY closed DESC")
        obsolete = []
        for row in cursor.fetchall():
            updated = UTC.timeparse(row['updated'])
            if now - updated > datetime.timedelta(days = 30):
                obsolete.append(row['sortkey'])
        if obsolete:
            with self.transaction() as txn:
                txn.con.executemany("DELETE FROM vote WHERE sortkey = ?",
                                    ((o,) for o in obsolete))


def main():
    parser = argparse.ArgumentParser(
        description = 'Generate Incubator voting status page.')
    parser.add_argument('mbox_archive', metavar = 'mbox-archive',
                        help = 'Path to the mailing list archives')
    parser.add_argument('--prune', dest='prune', action='store', default=None,
                        help='Pattern to prune from error messages (regex)')
    args = parser.parse_args()

    votes_path = SiteStructure.votes_database()
    if not os.path.isfile(votes_path):
        VoteDatabase.create(votes_path)

    archive_rx = re.compile(re.escape(args.mbox_archive))
    if args.prune:
        prune_rx = re.compile(args.prune)
    else:
        prune_rx = None

    def prune_error_message(message):
        match = archive_rx.search(message)
        if match:
            message = message[:match.start()] + '...' + message[match.end():]
        match = (prune_rx and prune_rx.search(message))
        if match:
            message = message[:match.start()] + '...' + message[match.end():]
        return message

    updater = VoteUpdater(args.mbox_archive)
    database = VoteDatabase(votes_path, prune_error_message)
    updater.record(database)
    database.prune_old_votes()
    database.close()

if __name__ == '__main__':
    main()
