#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import ConfigParser
import os


TOOLS_CFG_FILE = os.path.expanduser('~/.asf-tools.ini')


class load_config(object):
    def __init__(self, sections=None, defaults=None):
        defaults = defaults or {}
        self.config = ConfigParser.SafeConfigParser(defaults=defaults)
        self.config.read(TOOLS_CFG_FILE)

        if sections:
            for section in sections:
                if not self.config.has_section(section):
                    self.config.add_section(section)

    def get(self, section, option, raw=False, variables=None):
        return self.config.get(section, option, raw, variables)

    def set(self, section, option, value):
        self.config.set(section, option, value)

    def remove_option(self, section, option):
        self.config.remove_option(section, option)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if not exception_value:
            self.config.write(open(TOOLS_CFG_FILE, 'w'))
        return False
