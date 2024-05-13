"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_lst = [x for x in s]
        # s_lst.sort()
        # t_lst = [y for y in t]
        # t_lst.sort()
        # if len(s_lst) == len(t_lst):
        #     for i in range(len(s_lst)):
        #         if s_lst[i] != t_lst[i]:
        #             return False
        #     return True
        # else:
        #     return False

        counter_s, counter_t = {},{}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                counter_s[s[i]] = 1 + counter_s.get(s[i],0)
                counter_t[t[i]] = 1 + counter_t.get(t[i],0)
            for c in counter_s:
                if counter_s[c] != counter_t.get(c,0):
                    return False
            return True
        
        

