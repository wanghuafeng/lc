#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
参考主站 79题
https://leetcode-cn.com/problems/word-search/

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，
在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

示例 1：
    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    输出：true
示例 2：
    输入：board = [["a","b"],["c","d"]], word = "abcd"
    输出：false
提示：
    1 <= board.length <= 200
    1 <= board[i].length <= 200
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
        dp = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def traceback(board, row, col, word_index):
            if word_index == len(word) - 1: # 确定退出条件
                return board[row][col] == word[word_index]
            if board[row][col] == word[word_index]:
                dp[row][col] = True
                for directioin in directions:
                    new_row = row + directioin[0]
                    new_col = col + directioin[1]
                    if new_row >= 0 and new_row < len(board) and new_col >= 0 and new_col < len(board[0]) \
                            and not dp[new_row][new_col]\
                            and traceback(board, new_row, new_col, word_index+1):
                        return True
                dp[row][col] = False # 退出选择

        for row in range(len(board)):
            for col in range(len(board[0])):
                if traceback(board, row, col, 0):
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(Solution().exist(board, word))
