#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/spiral-matrix-ii/
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        l, r, t, b = 0, n-1, 0, n-1
        num = 1
        while True:
            for i in range(l, r+1):
                matrix[t][i] = num
                num += 1
            t += 1
            if t > b:
                break
            for i in range(t, b+1):
                matrix[i][r] = num
                num += 1
            r -= 1
            if r < l:
                break

            for i in range(r, l-1, -1):
                matrix[b][i] = num
                num += 1
            b -= 1
            if b < t:
                break

            for i in range(b, t-1, -1):
                matrix[i][l] = num
                num += 1
            l += 1
            if l > r:
                break
        return matrix

