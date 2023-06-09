class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i<len(nums)-3:
            j = i+1
            while j<len(nums)-2:
                k, l = j+1, len(nums)-1
                while k<l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k<l and nums[k] == nums[k+1]:
                            k += 1
                        while l>k and nums[l] == nums[l-1]:
                            l -= 1
                        k += 1
                        l -= 1
                    elif s < target:
                        k += 1
                    else:
                        l -= 1
                while j<len(nums)-2 and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            while i<len(nums)-3 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        

        return res
                



        
