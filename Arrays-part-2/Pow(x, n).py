class Solution:
    def myPow(self, x: float, n: int) -> float:
        res, neg = 1, 0
        if n<0:
            neg = 1
            n *= -1
        
        while n:
            if n&1:
                res *= x
            x *= x
            n >>= 1
        
        return res if not neg else 1/res

