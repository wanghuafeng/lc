#!-*- coding:utf-8 -*-
"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
示例 1:
    输入: 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:
    输入: 10
    输出: 36
    解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

说明: 你可以假设 n 不小于 2 且不大于 58。


解题思路:
    https://leetcode-cn.com/problems/integer-break/solution/bao-li-sou-suo-ji-yi-hua-sou-suo-dong-tai-gui-hua-/
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        res = -1
        for i in range(1, n):
            res = max(res, max(i*(n-i), i*self.integerBreak(n-i)))
        return res

class Solution(object):
    def __init__(self):
        self.dp = []

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp = [-1 for _ in range(n+1)]
        return self.helper(n)

    def helper(self, n):
        if n == 2:
            return 1
        if self.dp[n] != -1:    # 如果不为-1 表名已经计算过，直接返回
            return self.dp[n]
        res = -1
        for i in range(1, n):
            res = max(res, i*(n-i), i*self.helper(n-i))
        self.dp[n] = res
        return res



print Solution().integerBreak(10)