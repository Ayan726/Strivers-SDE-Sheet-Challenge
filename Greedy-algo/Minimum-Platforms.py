class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        if n == 1:
            return 1
        arr.sort()
        dep.sort()
        i, j = 1, 0
        cnt, maxi = 1, 1
        while i < n and j < n:
            if arr[i] <= dep[j]:
                cnt += 1
                i += 1
            else:
                cnt -= 1
                j += 1
            maxi = max(cnt, maxi)
        
        return maxi
                
