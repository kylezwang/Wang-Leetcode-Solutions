"""
Wang-Set-Matrix-Zeroes.py
    This program takes a matrix of ints and sets its columns and rows to 0
    if an element in the matrix is 0

by: Kyle Wang
August 3, 2023
"""
class Solution(object):
    def setZeroes(self, matrix):
# zeroCol list allows me to store the column indexes of 0 columns
        zeroCol = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    zeroCol.append(j)
# set entire row to 0's AFTER checking if the row originally has 0(s)
            if (matrix[i].count(0) > 0):
                matrix[i] = [0] * len(matrix[i])
# finally, replace all columns with 0's in the proper column index(es)
        for x in zeroCol:
            for z in range(len(matrix)):
                matrix[z][x] = 0
        

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
