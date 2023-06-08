class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        pairs = 0
        def merge(l, m, r, nums):
            nonlocal pairs
            j = m+1
            for i in range(l, m+1):
                while j<=r and nums[i] > 2*nums[j]:
                    j += 1
                pairs += j - m - 1

            res = []
            i, j = l, m+1
            while i<=m and j<=r:
                if nums[i] <= nums[j]:
                    res.append(nums[i])
                    i += 1
                else:
                    res.append(nums[j])
                    j += 1
            while i<=m:
                res.append(nums[i])
                i += 1
            while j<=r:
                res.append(nums[j])
                j += 1
            for i in range(l,r+1):
                nums[i] = res[i-l]

        def mergeSort(l, r, nums):
            if l>=r:
                return
            m = l + (r-l)//2
            mergeSort(l,m,nums)
            mergeSort(m+1,r,nums)
            merge(l,m,r,nums)
        
        mergeSort(0, len(nums) - 1, nums)
        return pairs
