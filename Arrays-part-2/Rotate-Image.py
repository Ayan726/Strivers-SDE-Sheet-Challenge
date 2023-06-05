class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        i, j = 0, 0
        n = len(mat)
        for i in range(n):
            x = i
            while x<n:
                mat[x][i], mat[i][x] = mat[i][x], mat[x][i]
                x += 1
        
        for j in range(n//2):
            for i in range(n):
                mat[i][j], mat[i][n-j-1] = mat[i][n-j-1], mat[i][j]
                


        
