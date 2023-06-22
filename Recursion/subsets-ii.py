class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()
        for i in range(1<<n):
            l = []
            for j in range(11):
                if ((i>>j)&1) == 1:
                    l.append(nums[j])
            res.add(tuple(l))
        
        return list(res)


        
