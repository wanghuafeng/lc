#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/valid-sudoku/
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [{} for i in range(9)]
        column = [{} for i in range(9)]
        box = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    box_index = (i / 3) * 3 + j / 3
                    row[i][num] = row[i].get(num, 0) + 1
                    column[j][num] = column[j].get(num, 0) + 1
                    box[box_index][num] = box[box_index].get(num, 0) + 1
                    if row[i][num] > 1 or column[j][num] > 1 or box[box_index][num] > 1:
                        return False
        return True
    