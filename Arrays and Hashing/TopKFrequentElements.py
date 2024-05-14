"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # res = {}
        # ans= []
        # for x in nums:
        #     res[x] = 1+res.get(x,0)
        # frequency = [x for x in res.values()]
        # frequency.sort(reverse=True)
        # most_freq = frequency[0:k]
        # for key, value in res.items():
        #     for x in most_freq:
        #         if value == x and key not in ans:
        #             ans.append(key)
        # return ans
        # Bucket Sorting APproach- Here each index reperesnts the count of the elemsnt
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1+count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(nums)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        