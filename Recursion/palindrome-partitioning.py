class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(x):
            return True if x == x[::-1] else False
        def dfs(ind, v):
            if ind  == len(s):
                res.append(v[:])
            x = ""
            for i in range(ind, len(s)):
                x += s[i]
                if isPalindrome(x):
                    v.append(x)
                    dfs(i+1, v[:])
                    v.pop()

        v = []
        dfs(0, v)
        return res
