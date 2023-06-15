class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        arr.sort(key= lambda x: (x.value/x.weight), reverse=True)
        res = 0
        
        for x in arr:
            if w >= x.weight:
                res += x.value
                w -= x.weight
            else:
                res += (x.value/x.weight)*w
                w = 0
                break
        
        return res
