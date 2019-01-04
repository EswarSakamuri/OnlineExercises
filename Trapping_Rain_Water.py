"""
Problem:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.
Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        for i in range(0,len(height)-1):
            print(height[i]-height[i+2])