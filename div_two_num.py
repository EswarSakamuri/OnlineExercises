"""
Problem:
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
"""

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res = 0
        chck = False
        temp = divisor
        if divisor < 0 and dividend < 0:
            temp = abs(divisor)
            divisor = abs(divisor)
            dividend = abs(dividend)
        elif divisor < 0 or dividend < 0:
            temp = abs(divisor)
            divisor = abs(divisor)
            dividend = abs(dividend)
            chck = True
        while divisor <= dividend:
            divisor+=temp
            res +=1
        if chck:
            return int("-"+str(res))
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.divide(-2147483648,-1))