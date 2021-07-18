"""
49. Group Anagrams
Difficulty: Medium
URL: https://leetcode.com/problems/group-anagrams/

Runtime Analysis: 
for val in strs loop increases wit N=len(strs)
0<strs[i]<100 = c is bounded by constant. Therefore, sort operation is O(c) = O(1)
O(c*N) = O(N)
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        agm_dict = {} #dictionary of immutable tuples. Sorted tuples for uniqueness
        for val in strs:
            #two strings are anagrams 
            #1)if they're not equal to each other
            #2) The count of each letter type are equal
            
            #anagrams can be track by dictionary
            #sorted tuple is immutable and can be used as key
            agm_tuple = tuple(sorted(val))
            #add to dictionary
            if agm_tuple in agm_dict: 
                agm_dict[agm_tuple].append(val)
            else:
                agm_dict[agm_tuple] = [val]
                
        #iterate over groups of sets
        #conver to list of lists
        res = []
        for key,myset in agm_dict.items():
            res.append(list(myset))
        return res
        