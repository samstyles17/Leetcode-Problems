"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # counter = {}
        # for x in nums:
        #     count = 1
        #     if x not in counter:
        #         counter.update({x:count})
        #     elif x in counter:
        #         counter.update({x:count+1})
        # count = [each for each in counter.values()]
        # if all(x == 1 for x in count):
        #     return False
        # else:
        #     return True

        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False
        

            
        