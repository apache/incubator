#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

from pypexels import PyPexels
from random import randint
import requests
import shutil, sys 

api_key = '563492ad6f91700001000001ba50a6850efa433e8b2324e5edb0df3d'
no_images = 20
city = "Sydney"

py_pexels = PyPexels(api_key=api_key)

city_photos = py_pexels.search(query=city,page=1,per_page=no_images)
index = 0
pic = randint(0,no_images-1)
for photo in city_photos.entries:
  if pic == index:
    print(photo.id, photo.photographer, photo.src["landscape"])
    headers = {'Authorization': api_key }
    response = requests.get(photo.src["landscape"], headers=headers, stream=True)
    with open(city+".jpg", 'wb') as image:
      shutil.copyfileobj(response.raw, image)
    del response
  index += 1
