"""
Problem:
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""


class Solution:
    def longestpalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l_pali = ""
        if len(s) > 1:
            for i in range(len(s)):
                for j in range(i+2, len(s)+1):
                    if s[i:j] == s[i:j][::-1] and len(s[i:j])>=len(l_pali):
                        l_pali = s[i:j]
            if len(l_pali) > 0:
                return l_pali
            return "Palindrome str not found"
        return s

if __name__ == "__main__":
    test_str = ["a", "babad", "cbbd", "bb"]
    s = Solution()
    for t in test_str:
        res = s.longestpalindrome(t)
        print(f"longest palindrome sub str of '{t}': ", res)
