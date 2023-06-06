class Solution:
    def merge(self, iv: List[List[int]]) -> List[List[int]]:
        iv.sort()
        maxi, mini = iv[0][1], iv[0][0]
        res = []
        for i in range(1, len(iv)):
            if iv[i][0] > maxi:
                res.append([mini, maxi])
                mini = iv[i][0]
                maxi = iv[i][1]
                continue
            mini = min(mini, iv[i][0])
            maxi = max(maxi, iv[i][1])
        
        res.append([mini, maxi])

        return res


