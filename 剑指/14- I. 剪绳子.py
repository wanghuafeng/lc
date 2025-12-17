#!-*- coding:utf-8 -*-
"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：
    输入: 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
    输入: 10
    输出: 36
    解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：
    2 <= n <= 58
"""
class Solution(object):
    def __init__(self):
        self.dp = []

    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp = [-1 for _ in range(n+1)]
        return self.helper(n)

    def helper(self, n):
        if n == 2:
            return 1
        if self.dp[n] != -1:
            return self.dp[n]
        res = 0
        for i in range(2, n):
            res = max(res, i*(n-i), i*self.helper(n-i))
        self.dp[n] = res
        return res
