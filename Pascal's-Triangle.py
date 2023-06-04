class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] for _ in range(numRows)]

        for i in range(1,numRows):
            for j in range(len(res[i-1])):
                res[i].append(res[i-1][j]+(res[i-1][j+1] if j+1<len(res[i-1]) else 0))
        

        return res
