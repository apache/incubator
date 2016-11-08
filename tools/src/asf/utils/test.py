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
import nose

from asf.utils.auth import get_stored_credentials


def ensure_credentials_stored(function):
    def wrapped(*args, **kwargs):
        username, password = get_stored_credentials()
        if not (username and password):
            raise nose.SkipTest('Credentials not stored for testing')

        return function(username, password, *args, **kwargs)

    return nose.tools.make_decorator(function)(wrapped)
