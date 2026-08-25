class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1
        row = 0
        while i <= j:
            mid = i + (j - i)//2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] > target:
                row = mid
                j = mid - 1
            else:
                row = mid + 1
                i = mid + 1
        if row >= len(matrix):
            return False
        
        i, j = 0, len(matrix[0]) - 1
        while i <= j:
            mid = i + (j - i)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False
        


