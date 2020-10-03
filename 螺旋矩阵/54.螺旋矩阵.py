#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/spiral-matrix/

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:
    输入:
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
    输出: [1,2,3,6,9,8,7,4,5]

示例 2:
    输入:
        [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]
        ]
    输出: [1,2,3,4,8,12,11,10,9,5,6,7]

"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        res = []
        while True:
            for i in range(l, r+1):   # 左到右
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break

            for j in range(t, b+1):   # 上到下
                res.append(matrix[j][r])
            r -= 1
            if r < l:
                break

            for m in range(r, l-1, -1):   # 右到左
                res.append(matrix[b][m])
            b -= 1
            if b < t:
                break

            for n in range(b, t-1, -1):	# 下到上
                res.append(matrix[n][l])
            l += 1
            if l > r:
                break

        return res