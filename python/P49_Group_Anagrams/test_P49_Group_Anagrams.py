import unittest
import P49_Group_Anagrams as _P49_Group_Anagrams
import P49_Group_Anagrams_submission2 as _P49_Group_Anagrams_submission2



class P49GroupAnagramsTestBase(object):
    @classmethod
    def setUpClass(cls):
        """To be defined by child class"""
        pass
    def setUp(self):
        pass
    #Answer can be returned in any order. 
    #add special assert function
    def _assertP49Equals(self,a,b):
        #sort a
        #sort inner list
        sorted_a = []
        for alist in a:
            sorted_a.append(sorted(alist))
        sorted_a.sort() #sort outer list
        if(self.DEBUG):
            print(sorted_a)

        sorted_b = []
        for blist in b:
            sorted_b.append(sorted(blist))
        sorted_b.sort() #sort outer list

        if(self.DEBUG):
            print(sorted_b)
        self.assertEqual(sorted_a,sorted_b)
        
    def test_solution_t1(self):
        # self.DEBUG = True
        self._assertP49Equals([["bat"],["nat","tan"],["ate","eat","tea"]],
        self.solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

    def test_solution_t2(self):
        # self.DEBUG = True
        self._assertP49Equals([[""]],self.solution.groupAnagrams([""]))

    def test_solution_t3(self):
        # self.DEBUG = True
        self._assertP49Equals([["a"]],self.solution.groupAnagrams(["a"]))

    def test_solution_t4(self):
        # self.DEBUG = True
        self._assertP49Equals([["odor","rood","door"],["act","cat"]],self.solution.groupAnagrams(["cat","door","act","odor","rood"]))


class P49GroupAnagramsTestCase(unittest.TestCase,P49GroupAnagramsTestBase):
    @classmethod
    def setUpClass(cls):
        cls.solution = _P49_Group_Anagrams.Solution()
    def setUp(self):
        self.DEBUG = False

class P49GroupAnagramsSubmission2TestCase(unittest.TestCase,P49GroupAnagramsTestBase):
    @classmethod
    def setUpClass(cls):
        cls.solution = _P49_Group_Anagrams_submission2.Solution()
    def setUp(self):
        self.DEBUG = False
