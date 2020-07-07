#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/word-search/

给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 
提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右四个方向
         # 初始化二维数组的时候总是出错，下次提前想清楚
        visited_matrix = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        def traceback(board, row, col, word_index):
            if word_index == len(word) - 1:
                return board[row][col] == word[word_index]
            if board[row][col] == word[word_index]: # 当前元素匹配
                visited_matrix[row][col] = True  # 已访问过，做标记
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    # 1.行列边界问题; 2.是否被标记;
                    if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) \
                        and not visited_matrix[new_row][new_col]\
                        and traceback(board, new_row, new_col, word_index+1):
                            return True
                visited_matrix[row][col] = False   # 撤回状态标记

        for i in range(len(board)):
            for j in range(len(board[0])):
                if traceback(board, i, j, 0):
                    return True
        return False


board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word = "ABCB"
print Solution().exist(board, word)