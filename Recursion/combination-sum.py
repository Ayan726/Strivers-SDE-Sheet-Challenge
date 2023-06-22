class Solution:
    def combinationSum(self, cd: List[int], target: int) -> List[List[int]]:
        cd.sort()
        res = set()
        l = []
        def dfs(ind, s):
            nonlocal res, l
            if s > target:
                return
            if s == target:
                res.add(tuple(l))
                return
            if ind == len(cd):
                return
                
            l.append(cd[ind])
            dfs(ind, s+cd[ind])
            l.pop()
            dfs(ind+1, s)
        
        dfs(0, 0)
        return list(res)
        

            
            
