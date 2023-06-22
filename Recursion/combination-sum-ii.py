class Solution:
    def combinationSum2(self, arr: List[int], k: int) -> List[List[int]]:
        arr.sort()
        res, l = [], []
        def dfs(ind,s):
            nonlocal res, l
            if s > k:
                return
            if s == k:
                res.append(l.copy())
                return
            if ind == len(arr):
                return
            if arr[ind] > k:
                return
            for i in range(ind, len(arr)):
                if i != ind and arr[i] == arr[i-1]:
                    continue
                l.append(arr[i])
                dfs(i+1, s+arr[i])
                l.pop()

        dfs(0,0)
        return res


