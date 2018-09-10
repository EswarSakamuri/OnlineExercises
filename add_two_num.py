"""
Problem:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r_l1 = ""
        for l in l1:
            r_l1 += str(l)
        r_l1 = int(r_l1)

        r_l2 = ""
        for l in l2:
            r_l2 += str(l)
        r_l2 = int(r_l2)

        sum = str(r_l1+r_l2)
        print(sum)
        res = []
        for s in sum[::-1]:
            res.append(int(s))
        return res


if __name__ == "__main__":
    s = Solution()
    a = s.addTwoNumbers([2,4,3], [5,6,4])
    print(a)