class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # circular swapping
        i = 0
        while i < len(nums):
            while nums[i] != i+1:
                if nums[nums[i] - 1] == nums[i]:
                    return nums[i]
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            i += 1
        
        return -1

        # hare & tortoise method
        hare, turtle = nums[0], nums[0]
        hare = nums[nums[hare]]
        turtle = nums[turtle]
        
        while hare != turtle:
            hare = nums[nums[hare]]
            turtle = nums[turtle]
        hare = nums[0]

        while hare != turtle:
            hare = nums[hare]
            turtle = nums[turtle]
        
        return hare


