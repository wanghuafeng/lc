#!-*- coding:utf-8 -*-
"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
    X X X X
    X O O X
    X X O X
    X O X X

运行你的函数后，矩阵变为：
    X X X X
    X X X X
    X X X X
    X O X X

解释:
    被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
    任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
    如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。


思路: 有限处理边界
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return []
        m = len(board)
        n = len(board[0])

        def infect(board, i, j):
            if i<0 or i >=m or j<0 or j>=n or board[i][j] != 'O':
                return
            board[i][j] = '1'
            infect(board, i+1, j)
            infect(board, i-1, j)
            infect(board, i, j-1)
            infect(board, i, j+1)

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n - 1:  # 边界
                    if board[i][j] == 'O':
                        infect(board, i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '1':
                    board[i][j] = 'O'
        return board


board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]

print Solution().solve(board)
