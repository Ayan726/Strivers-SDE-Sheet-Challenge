class Solution:
	def subsetSums(self, arr, n):
	    res = []
	    def dfs(ind, s):
	        nonlocal res
	        if ind == n:
	            res.append(s)
	            return 
	        dfs(ind+1, s)
	        dfs(ind+1, s+arr[ind])
	    
	    dfs(0,0)
	    return sorted(res)
