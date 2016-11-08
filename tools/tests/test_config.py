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
import contextlib
import os

from mock import patch

from asf.utils.config import load_config
from asf.utils.file import temp_directory


@contextlib.contextmanager
def mock_tools_config_file():
    with temp_directory() as tmp_dir:
        mock_tools_cfg_file = os.path.join(tmp_dir, 'asf-tools.ini')

        with patch('asf.utils.config.TOOLS_CFG_FILE', new=mock_tools_cfg_file):
            yield mock_tools_cfg_file


def test_config_file_creation():
    with mock_tools_config_file() as mock_tools_cfg_file:
        assert not os.path.exists(mock_tools_cfg_file)

        with load_config([], {}) as config:
            pass

        assert os.path.exists(mock_tools_cfg_file)


def test_config_section_creation():
    with mock_tools_config_file() as mock_tools_cfg_file:
        assert not os.path.exists(mock_tools_cfg_file)

        with load_config(['TEST-SECTION'], {}) as config:
            pass

        config = ConfigParser.SafeConfigParser()
        config.read(mock_tools_cfg_file)

        assert len(config.sections()) == 1
        assert 'TEST-SECTION' in config.sections()


def test_config_defaults():
    with mock_tools_config_file() as mock_tools_cfg_file:
        assert not os.path.exists(mock_tools_cfg_file)

        with load_config(sections=['TEST-SECTION']) as config:
            config.set('TEST-SECTION', 'c', 'not_d')

        with load_config(sections=['TEST-SECTION'], defaults={'a': 'b', 'c': 'd'}) as config:
            assert config.get('TEST-SECTION', 'a') == 'b'
            assert config.get('TEST-SECTION', 'c') == 'not_d'
