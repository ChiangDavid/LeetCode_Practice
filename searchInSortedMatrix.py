#74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Brute Force
# O(N^2)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        one_d_arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                one_d_arr.append(matrix[i][j])

        left, right = 0, len(one_d_arr) - 1 
        while left <= right:
            mid = (left+right) // 2
            if one_d_arr[mid] == target:
                return True
            elif one_d_arr[mid] > target:
                right = mid - 1
            else: 
                left = mid + 1
        return False
      
#Binary Search
#  O(log(m * n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            left, right = 0, cols-1
            while left <= right:
                mid = (left+right)//2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
