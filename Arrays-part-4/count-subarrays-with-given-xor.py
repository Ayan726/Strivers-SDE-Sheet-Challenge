from collections import *
def subarraysXor(arr, x):
    dic = defaultdict(int)
    dic[0] = 1
    s, res = 0, 0
    for i in range(len(arr)):
        s ^= arr[i]
        if (x^s) in dic:
            res += dic[x^s]
        dic[s] += 1
    
    return res


