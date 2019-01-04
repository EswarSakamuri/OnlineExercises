class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(candidates);
        candidates.sort()
        ans = []

        def foo(index, cur, path):
            if cur == 0:
                ans.append(path)
                return
            last = None
            for i in range(index + 1, l):
                temp = candidates[i]
                if temp > cur: break
                if temp == last: continue
                last = temp
                foo(i, cur - temp, path + [temp])

        foo(-1, target, [])
        return ans



if __name__ == "__main__":
    s= Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))