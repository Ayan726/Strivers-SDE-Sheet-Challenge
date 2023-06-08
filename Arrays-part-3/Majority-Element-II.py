class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 2 2 3 4 3 3 
        el1, el2, c1, c2, n = -1e9-7,-1e9-7,0,0,len(nums)
        for x in nums:
            if x == el1:
                c1 += 1
            elif x == el2:
                c2 += 1
            elif not c1:
                el1 = x
                c1 = 1
            elif not c2:
                el2 = x
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        res = []
        if nums.count(el1) > n//3:
            res.append(el1)
        if nums.count(el2) > n//3:
            res.append(el2)
        return res
