class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el, cnt = -1, 0

        for x in nums:
            if not cnt:
                el = x
            if x == el:
                cnt += 1
            else:
                cnt -= 1
        
        return el
            
