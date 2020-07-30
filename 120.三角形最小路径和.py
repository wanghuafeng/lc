#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/triangle/

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
例如，给定三角形：
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
    如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

解题思路:
    相邻结点：与(i, j) 点相邻的结点为 (i + 1, j) 和 (i + 1, j + 1)。

分析：
    若定义 f(i, j)f(i,j) 为 (i, j)(i,j) 点到底边的最小路径和，则易知递归求解式为:
    f(i, j) = min(f(i + 1, j), f(i + 1, j + 1)) + triangle[i][j]

1.递归 (超时)
2.二维数据动态规划
3.一维位数组动态规划
"""

class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return self.dfs(triangle, 0, 0)

    def dfs(self, triangle, row, col):
        if row == len(triangle):
            return  0
        return min(self.dfs(triangle, row+1, col), self.dfs(triangle, row+1, col+1)) + triangle[row][col]


class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp = [[0]*len(triangle) for _ in range(len(triangle))]
        dp[-1] = triangle[-1]
        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                dp[row][col] = min(dp[row+1][col], dp[row+1][col+1]) + triangle[row][col]
        return dp[0][0]


l = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print Solution().minimumTotal(l)