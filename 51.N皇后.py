#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/n-queens/

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
     [".Q..",  // 解法 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // 解法 2
      "Q...",
      "...Q",
      ".Q.."]
    ]

回溯法:
    result = []
    def backtrack(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return

        for 选择 in 选择列表:
            做选择
            backtrack(路径, 选择列表)
            撤销选择
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        matrix = [['.']*n for _ in range(n)]
        res = []
        def traceback(matrix, row):
            if row == n:
                tmp = []
                for i in range(n):
                    tmp.append(''.join(matrix[i]))
                res.append(tmp)
                return
            for col in range(n):
                if not queen_valid(matrix, row, col):
                    continue
                # 选择分支
                matrix[row][col] = 'Q'
                # 递归
                traceback(matrix, row+1)
                # 回退
                matrix[row][col] = '.'

        def queen_valid(matrix, row, col):
            # 因为row+1为新行，不可能有皇后，所以这里考虑"列"是否有皇后冲突
            for i in range(row):
                if matrix[i][col] == 'Q':
                    return False
            i, j = row, col
            # 右上方皇后校验
            while  i >= 0 and j < n:
                if matrix[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            i, j = row, col
            # 左上方皇后校验
            while i >= 0 and j >= 0:
                if matrix[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 没有皇后冲突，说明该位置可以选择
            return True
        traceback(matrix, 0)
        return res