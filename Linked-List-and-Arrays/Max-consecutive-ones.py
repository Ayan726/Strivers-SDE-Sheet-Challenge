class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i, maxi = 0, 0

        while i<len(nums):
            if not nums[i]:
                i += 1
                continue
            x = 0
            while i+1<len(nums) and nums[i] == nums[i+1]:
                x += 1
                i += 1
            maxi = max(x+1, maxi)
            i += 1
        return maxi
