#########################################################################################
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#########################################################################################

import xml.parsers.expat
import os
import os.path
import subprocess

class InvalidDocument(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)
        
class Document:
    def __init__(self):
        self.reset()
        
    def __str__(self):
        return self.name + "," + self.dir
        
    def reset(self):
        self.next = None
        self.dir = None
        self.name = None
        self.md5 = None
        self.sha = None
        self.ripemd= None
        
    def __setMd5(self, value):
        if self.md5 == None:
            self.md5 = value
        else:
            self.md5 = self.md5 + value
        
    def __setSha(self, value):
        if self.sha == None:
            self.sha = value
        else:
            self.sha = self.sha + value

    def __setRipemd(self, value):
        if self.ripemd == None:
            self.ripemd = value
        else:
            self.ripemd = self.ripemd + value
        
    def start_element(self, name, attrs):
        if name == 'document':
            self.name = attrs.get('name')
            self.dir = attrs.get('dir')
        elif name == 'md5':
            self.next = self.__setMd5
        elif name == 'sha512':
            self.next = self.__setSha
        elif name == 'ripemd160':
            self.next = self.__setRipemd
        else:
            self.next = None
    
    def end_element(self, name):
        pass
    
    def char_data(self, data):
        if not self.next == None:
            self.next(data.strip())
        
    def match(self, documents):
        for document in documents:
            if document.name == self.name and document.dir == self.dir:
                return document
        return None 
            
    def isMissing(self, documents):
        return self.match(documents) == None
        
    def isModified(self, documents):
        document = self.match(documents)
        if document == None:
            return False
        else:
            return not (document.md5 == self.md5 and document.sha == self.sha 
                        and document.ripemd == self.ripemd)
            
    def summaryXml(self):
        return '<document name="' + self.name + '" dir="' + self.dir + '"/>'
    
def document(dir, name, md5, sha, ripemd):
    result = Document()
    result.dir = dir
    result.name = name
    result.md5 = md5
    result.sha = sha
    result.ripemd = ripemd
    return result
            
class Documents:
    def __init__(self):
        self.documents = []
        self.__current = None
        
    def append(self, document):
        self.documents.append(document)
        
    def load(self, document):
        self.documents = []
        self.__current = None
        self.on = None
        parser = xml.parsers.expat.ParserCreate()
        parser.StartElementHandler = self.start_element
        parser.EndElementHandler = self.end_element
        parser.CharacterDataHandler = self.char_data
        parser.Parse(document)
    
    def start_element(self, name, attrs):
        if name == 'audit':
            self.on = attrs.get('on')
        if name == 'document':
            self.__current = Document()
            self.documents.append(self.__current)
            self.__current.start_element(name, attrs)
        elif not self.__current == None:
            self.__current.start_element(name, attrs)
            
    def end_element(self, name):
        if not self.__current == None:
            self.__current.end_element(name)
        if name == 'document':
            self.__current = None
        
    def char_data(self, data):
        if not self.__current == None:
            self.__current.char_data(data)
            
    def __iter__(self):
        for document in self.documents:
            yield(document)
            
    def isModified(self, document):
        return document.isModified(self.documents)
    
    def isMissing(self, document):
        return document.isMissing(self.documents)
            
    def compare(self, documents):
        added = filter(documents.isMissing, self)
        removed = filter(self.isMissing, documents)
        modified = filter(documents.isModified, self)
        return added, removed, modified
    
def documents(documents):
    results = Documents()
    for document in documents:
        results.append(document)
    return results

class Auditor:
    def __init__(self, basedir):
        self.basedir = basedir
        
    def printSignatureChecks(self):
        for file in os.listdir(self.basedir):
            if file.endswith('.asc'):
                print file
                subprocess.Popen('gpg --verify ' + os.path.join(self.basedir, file), shell=True).wait()
                print
                
    def load(self, name):
        f = open(os.path.join(self.basedir, name), 'r')
        try:
            documents = Documents()
            documents.load(f.read())
            if not documents.on == name[-14:-4]:
                raise InvalidDocument('Document date does not match file date.')
            return documents
        finally:
            f.close()
            
    def latest(self):
        xmlDocuments = filter(lambda x:x.endswith('.xml'), os.listdir(self.basedir))
        xmlDocuments.sort()
        return map(self.load, xmlDocuments[-2:])
                
    def latestDiffs(self):
        latest = self.latest()
        return self.diffs(latest[1], latest[0])
        
    def diffs(self, one, two):
        added, removed, modified = one.compare(two)
        toXml = lambda a, name: simpleElement(name, reduce(lambda b, c: b + c, map(lambda x: x.summaryXml(), a), ''))
        diff = toXml(added, 'added') + toXml(modified, 'modified') + toXml(removed, 'missing')
        return '<changes from="' + two.on + '" to="' + one.on + '">' + diff + '</changes>' 
                
def simpleElement(element, body):
    return startTag(element) + body + endTag(element)
                
def startTag(element):
    return '<' + element + '>'
 
def endTag(element):
    return '</' + element + '>'
                
if __name__ == '__main__':
    auditor = Auditor('audit')
    auditor.printSignatureChecks()
    print auditor.latestDiffs()