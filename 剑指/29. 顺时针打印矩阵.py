#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,6,9,8,7,4,5]

示例 2：
    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        res = []
        while True:
            for i in range(left, right+1):
                val = matrix[top][i]
                res.append(val)
            top += 1
            if top > bottom:
                break
            for j in range(top, bottom + 1):
                val = matrix[j][right]
                res.append(val)
            right -= 1
            if right < left:
                break
            for i in range(right, left-1, -1):
                val = matrix[bottom][i]
                res.append(val)
            bottom -= 1
            if bottom < top:
                break
            for i in range(bottom, top-1, -1):
                val = matrix[i][left]
                res.append(val)
            left += 1
            if left > right:
                break
        return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print Solution().spiralOrder(matrix)