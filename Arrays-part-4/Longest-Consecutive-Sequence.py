class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] = i

        vis = [0]*len(nums)
        dp = defaultdict(int)

        def dfs(node):
            nonlocal vis, dic, dp
            if node in dp:
                return dp[node]
            vis[node] = 1
            x = nums[node]
            ans = 1
            if x+1 in dic:
                ans += dfs(dic[x+1])
            dp[node] = ans
            return ans

        maxi = 0

        for i in range(len(nums)):
            if not vis[i]:
                maxi = max(maxi, dfs(i))
        return maxi

        
