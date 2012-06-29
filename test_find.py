import unittest
import ipdb
from find import *

class TestFind(unittest.TestCase):

    def setUp(self):
        self.ctree = tree()
        self.ctree.generate(self.ctree.root,2,0,"/1")

    def tearDown(self):
        pass

    def test_FindExact(self):
        temp = find_exact('8', self.ctree)
        self.assertEqual(temp, "/1/6/8")

#    def test_FindSingle(self):
#        temp = find("100?00", self.ctree)
#        ipdb.set_trace()
#	self.assertEqual(temp, [])
#        pass
#    def test_FindMultiple(self):
#        temp = find("12*1", self.ctree)
#	self.assertEqual(temp, ['1212', '12'])
#        pass
#    def test_FindSpecified(self):
#        temp = find("12[0123]", self.ctree)
#        self.assertEqual(temp, ['120', '121', '123'])
#        pass
#    def test_FindDirExact(self):
#        temp = find_dir("3", self.ctree.root)
#	self.assertEqual(temp, "/1/2/3")
#        pass
#    def test_FindDirSingle(self):
#        temp = find_dir("1?", self.ctree.root)
#	self.assertEqual(temp, ["10", '11', '12', '13', '14', '15', '16', '17', '18', '19'])
#        self.assertEqual(temp, [])
#        pass
#    def test_FindDirMultiple(self):
#        temp = find_dir("100*00", self.ctree.root)
#       self.assertEqual(temp, ["100", "1000", "10000"])
#        pass
#    def test_FindDirSpecified(self):
#        temp = find_dir("[01234]", self.ctree.root)
#        self.assertEqual(temp, ['1', '2', '3', '4'])
#        pass
