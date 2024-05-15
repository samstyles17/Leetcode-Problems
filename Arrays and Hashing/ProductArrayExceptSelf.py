"""
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

class Solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        # This approach does not follow O(n) time complexity constraint 
        """""
        answer = []
        for i, x in enumerate(nums):
            temp_nums = [nums[y] for y in range(len(nums)) if y != i]
            prod = 1
            for each in temp_nums:
                prod *= each
            answer.append(prod)
        return answer
        """
        # This approach follows O(n) time complexity by considering the prefix and postfix product for each index and multipying them
        # Here, prefix product is calculated and stored first for each index and then multiplied with postfix product
        answer = [1] * len(nums)
        prefix =1 # For the first element, since there is no  prefix default prefix is 1
        for i in range(len(nums)):
            answer[i] = prefix
            # Next the prefix is updated for the next iteration
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer
