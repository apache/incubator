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

import scanner
import unittest
import diff
import xml.parsers.expat

class ReadXmlTestCase(unittest.TestCase):
    
    def testReadOne(self):
        document = diff.Document()
        parser = xml.parsers.expat.ParserCreate()
        parser.StartElementHandler = document.start_element
        parser.EndElementHandler = document.end_element
        parser.CharacterDataHandler = document.char_data
        parser.Parse("""<?xml version="1.0"?>
 <document dir='a directory' name='a name' >
  <md5>MD5 SUM</md5>
  <sha512>SHA SUM</sha512>
  <ripemd160>RIPEMD</ripemd160>
 </document>""", 1)
        
        self.assertEqual('a directory', document.dir)
        self.assertEqual('a name', document.name)
        self.assertEqual('MD5 SUM', document.md5)
        self.assertEqual('SHA SUM', document.sha)
        self.assertEqual('RIPEMD', document.ripemd)
        
    def testLoad(self):
        documents = diff.Documents()
        documents.load("""<?xml version="1.0"?><audit on='2008-01-22'><documents>
 <document dir='a directory' name='a name' >
  <md5>MD5 SUM</md5>
  <sha512>SHA SUM</sha512>
  <ripemd160>RIPEMD</ripemd160>
 </document>
  <document dir='another directory' name='another name' >
  <md5>ANOTHER MD5 SUM</md5>
  <sha512>ANOTHER SHA SUM</sha512>
  <ripemd160>ANOTHER RIPEMD</ripemd160>
 </document>
 </documents></audit>
 """)
        
        self.assert_(not documents.documents == None)
        self.assertEqual('2008-01-22', documents.on)
        self.assertEqual(2, len(documents.documents))
        document = documents.documents[0]
        self.assertEqual('a directory', document.dir)
        self.assertEqual('a name', document.name)
        self.assertEqual('MD5 SUM', document.md5)
        self.assertEqual('SHA SUM', document.sha)
        self.assertEqual('RIPEMD', document.ripemd)
        document = documents.documents[1]
        self.assertEqual('another directory', document.dir)
        self.assertEqual('another name', document.name)
        self.assertEqual('ANOTHER MD5 SUM', document.md5)
        self.assertEqual('ANOTHER SHA SUM', document.sha)
        self.assertEqual('ANOTHER RIPEMD', document.ripemd)
        
class DiffTestCase(unittest.TestCase):
    def setUp(self):
        self.documents = []
        self.documents.append(diff.document("dir", "name", "md5", "sha", "ripemd"))
        self.document2 = diff.document("dir", "name2", "2md5", "2sha", "2ripemd")
        self.documents.append(self.document2)
        self.documents.append(diff.document("dirA", "name", "Amd5", "Asha", "Aripemd"))
        self.documents.append(diff.document("dirA", "nameB", "Bmd5", "Bsha", "Bripemd"))
        
    def testIsMissing(self):
        document = diff.document("dir", "name", "md5", "sha", "ripemd")
        self.assertEquals(False, document.isMissing(self.documents))
        document = diff.document("dirA", "name", "Amd5", "Asha", "Aripemd")
        self.assertEquals(False, document.isMissing(self.documents))      
        document = diff.document("dirC", "name", "md5", "sha", "ripemd")
        self.assertEquals(True, document.isMissing(self.documents))
        document = diff.document("dir", "nameB", "md5", "sha", "ripemd")
        self.assertEquals(True, document.isMissing(self.documents))
        
    def testIsModified(self):
        document = diff.document("dir", "name", "md5", "sha", "ripemd")
        self.assertEquals(False, document.isModified(self.documents))
        document = diff.document("dirA", "name", "Amd5", "Asha", "Aripemd")
        self.assertEquals(False, document.isModified(self.documents))      
        document = diff.document("dirC", "name", "md5", "sha", "ripemd")
        self.assertEquals(False, document.isModified(self.documents))
        document = diff.document("dir", "nameB", "md5", "sha", "ripemd")
        self.assertEquals(False, document.isModified(self.documents))
        document = diff.document("dir", "name", "Amd5", "sha", "ripemd")
        self.assertEquals(True, document.isModified(self.documents))
        document = diff.document("dir", "name", "md5", "Qsha", "ripemd")
        self.assertEquals(True, document.isModified(self.documents))
        document = diff.document("dir", "name", "md5", "sha", "Tripemd")
        self.assertEquals(True, document.isModified(self.documents))
        
    def testCompareEmpty(self):
        emptyDocuments = diff.Documents()
        documents = diff.documents(self.documents)
        added, removed, modified = documents.compare(emptyDocuments)
        self.assert_(not added == None)
        self.assert_(not removed == None)
        self.assert_(not modified == None)
        self.assertEquals(4, len(added))
        self.assertEquals(0, len(modified))
        self.assertEquals(0, len(removed))
        added, removed, modified = emptyDocuments.compare(documents)
        self.assert_(not added == None)
        self.assert_(not removed == None)
        self.assert_(not modified == None)
        self.assertEquals(0, len(added))
        self.assertEquals(0, len(modified))
        self.assertEquals(4, len(removed))
        
    def testCompareDiffering(self):
        documents = diff.documents(self.documents)
        
        differentsDocuments = diff.Documents()
        modifiedDocument = diff.document("dir", "name", "NOT", "NOT", "NOT")
        newDocument = diff.document("anotherdir", "anothername", "NOT", "NOT", "NOT")
        differentsDocuments.append(modifiedDocument)
        differentsDocuments.append(newDocument)
        differentsDocuments.append(diff.document("dirA", "name", "Amd5", "Asha", "Aripemd"))
        differentsDocuments.append(diff.document("dirA", "nameB", "Bmd5", "Bsha", "Bripemd"))
        
        added, removed, modified = differentsDocuments.compare(documents)
        self.assert_(not added == None)
        self.assert_(not removed == None)
        self.assert_(not modified == None)
        self.assertEquals(1, len(modified))
        self.assertEquals(1, len(added))
        self.assertEquals(1, len(removed))
        self.assertEquals(modifiedDocument, modified[0])
        self.assertEquals(newDocument, added[0])
        self.assertEquals(self.document2, removed[0])