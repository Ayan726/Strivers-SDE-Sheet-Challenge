class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res, arr = "", [i for i in range(1,n+1)]
        fact = [1]
        for i in range(1, n+1):
            fact.append(i*fact[-1])
        # print(fact)
        while n:
            x = fact[n]
            x //= n
            ind = ceil(k/x)
            res += str(arr.pop(ind-1)) # for ind == 0 it will pop the -1th element which is last element in python
            k %= x
            n -= 1
        
        return res

