import unittest
from P49_Group_Anagrams import Solution
class P49GroupAnagramsTestCase(unittest.TestCase):

    def setUp(self):
        self.debug = False
    #Answer can be returned in any order. 
    #add special assert function
    def _assertP49Equals(self,a,b):
        #sort a
        #sort inner list
        sorted_a = []
        for alist in a:
            sorted_a.append(sorted(alist))
        sorted_a.sort() #sort outer list
        if(self.debug):
            print(sorted_a)

        sorted_b = []
        for blist in b:
            sorted_b.append(sorted(blist))
        sorted_b.sort() #sort outer list

        if(self.debug):
            print(sorted_b)
        self.assertEqual(sorted_a,sorted_b)
        
    def test_solution_t1(self):
        # self.debug = True
        self._assertP49Equals([["bat"],["nat","tan"],["ate","eat","tea"]],
        Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

    def test_solution_t2(self):
        # self.debug = True
        self._assertP49Equals([[""]],Solution().groupAnagrams([""]))

    def test_solution_t3(self):
        # self.debug = True
        self._assertP49Equals([["a"]],Solution().groupAnagrams(["a"]))

    def test_solution_t4(self):
        # self.debug = True
        self._assertP49Equals([["odor","rood","door"],["act","cat"]],Solution().groupAnagrams(["cat","door","act","odor","rood"]))