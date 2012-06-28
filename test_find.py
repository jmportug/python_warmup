import unittest
import ipdb
from find import *

class TestFind(unittest.TestCase):

    def setUp(self):
        self.ctree = tree()
        self.ctree.generate(self.ctree.root)

    def tearDown(self):
        pass

    def test_FindExact(self):
        # This actually works when commenting out the other tests so that only
        # this runs. It seems that one or more of the other tests does something that modifies the tree, causing this to fail.
        # I noticed something similar when running the find_demo -- at one point 
        # f 8 wasn't working, but when I restarted it started working again.
        temp = find_exact('8', self.ctree)
        self.assertEqual(temp, "/1/2/3/4/5/6/7/8")

    def test_FindSingle(self):
        temp = find("100?00", self.ctree)
#        ipdb.set_trace()
#       self.assertEqual(temp, [])

    def test_FindMultiple(self):
        temp = find("12*1", self.ctree)
#       self.assertEqual(temp, ['1212', '12'])

    def test_FindSpecified(self):
        temp = find("12[0123]", self.ctree)
#        self.assertEqual(temp, ['120', '121', '123'])

    def test_FindDirExact(self):
        # Be careful about mixing tabs and spaces. This probably looked fine 
        # for you because you have 1 tab = 8 spaces.
        temp = find_dir("3", self.ctree.root)
        self.assertEqual(temp, "/1/2/3")

    def test_FindDirSingle(self):
        temp = find_dir("1?", self.ctree.root.sub_dirs[3])
        self.assertEqual(temp, ["10", '11', '12', '13', '14', '15', '16', '17', '18', '19'])
#        print(temp)
#        ipdb.set_trace()
#        self.assertEqual(temp, [])

    def test_FindDirMultiple(self):
        temp = find_dir("100*00", self.ctree.root)
        # One problem here is that your array contains ints instead of 
        # string-numbers, but it also seems to be missing part of the result.
        self.assertEqual(temp, ['100', '1000'])

    def test_FindDirSpecified(self):
        temp = find_dir("[01234]", self.ctree.root)
        self.assertEqual(temp, ['1', '2', '3', '4'])
