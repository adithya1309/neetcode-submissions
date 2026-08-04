class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        for cell in matrix:
            left = 0
            right = len(cell) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if cell[mid] == target:
                    return True
                elif cell[mid] > target:
                    right = mid - 1
                elif cell[mid] < target:
                    left = mid + 1
        return False