class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l<=r:
            m = l + (r-l)//2
            if matrix[m][0] == target:
                return True
            if matrix[m][0] > target:
                r = m-1
            else:
                l = m+1
        
        ind = bisect_left(matrix[r], target)

        if ind == len(matrix[r]) or matrix[r][ind] != target:
            return False
        return True



