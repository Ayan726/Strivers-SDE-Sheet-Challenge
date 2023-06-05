class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        ind = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind = i
                break
        
        i = len(nums)-1
        while i>ind and ind!=-1:
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break
            i -= 1
        
        nums[ind+1:] = reversed(nums[ind+1:])

                
