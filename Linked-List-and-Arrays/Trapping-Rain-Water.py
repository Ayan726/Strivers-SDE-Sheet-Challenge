class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r, lmax, rmax = 0, n-1, 0, 0
        res = 0
        while l<=r:
            if height[l] <= height[r]:
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    res += lmax-height[l]
                l += 1
            else:
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    res += rmax - height[r]
                r -= 1
        
        return res



        


            




