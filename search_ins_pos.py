"""
Problem:
Given a sorted array and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > max(nums):
            return len(nums)
        elif target < min(nums):
            return 0
        if target in nums:
            return nums.index(target)
        else:
            return optimal_inx(nums, target)

def optimal_inx(nums, target):
    min_indx = 0
    for n in nums:
        if n<target:
            min_indx = nums.index(n)
            min_indx+=1
    return min_indx

if __name__ == "__main__":
    s= Solution()
    print(s.searchInsert([1,3,5,6], 0))