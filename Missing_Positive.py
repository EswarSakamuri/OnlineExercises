"""
Problem
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
"""
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        nums = [n for n in nums if n >= 0]
        nums.sort()
        if len(nums) <= 0:
            return 1
        for j in range(1, len(nums) + 1):
            if j not in nums:
                return j

        return j+1



if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([3, 4, -1, 1]))
