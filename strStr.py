"""
Problem:
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


import re

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if re.search(needle,haystack):
            return haystack.index(needle)
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.strStr("aaaaa", "bba"))
