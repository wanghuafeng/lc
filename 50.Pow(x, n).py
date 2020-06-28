#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/powx-n/
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:
    输入: 2.00000, 10
    输出: 1024.00000
示例 2:
    输入: 2.10000, 3
    输出: 9.26100
示例 3:
    输入: 2.00000, -2
    输出: 0.25000

说明:
    -100.0 < x < 100.0
    n 是 32 位有符号整数
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        """
        def multi(x, n):
            if n == 0:
                return 1
            y = multi(x, n/2)
            if n % 2 == 0:
                ans = y * y
            else:
                ans = y * y * x
            return ans
        return multi(x, n) if n > 0 else 1/multi(x, -n)

