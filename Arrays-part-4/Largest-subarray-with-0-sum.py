from collections import *

class Solution:
    def maxLen(self, n, arr):
        dic = defaultdict(int)
        dic[0] = -1
        s, maxi = 0, 0
        for i in range(len(arr)):
            s += arr[i]
            if s in dic:
                maxi = max(maxi, i-dic[s])
            else:
                dic[s] = i
        
        return maxi
                
