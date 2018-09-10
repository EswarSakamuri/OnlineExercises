"""
Problem:
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""


class Solution:
    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        data_set = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        digit_str = str(digits)



if __name__ == "__main__":
    s = Solution()
    print(s.letter_combinations(29))