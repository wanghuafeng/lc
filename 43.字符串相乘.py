#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/multiply-strings/

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:
    输入: num1 = "2", num2 = "3"
    输出: "6"

示例 2:
    输入: num1 = "123", num2 = "456"
    输出: "56088"

说明：
    num1 和 num2 的长度小于110。
    num1 和 num2 只包含数字 0-9。
    num1 和 num2 均不以零开头，除非是数字 0 本身。
    不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

乘数 num1 位数为 MM，被乘数 num2 位数为 NN， num1 x num2 结果 res 最大总位数为 M+N
num1[i] x num2[j] 的结果为 tmp(位数为两位，"0x","xy"的形式)，
其第一位位于 res[i+j]，第二位位于 res[i+j+1]。
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        n1 = len(num1)
        n2 = len(num2)
        res = [0] * (n1+n2)
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                sum_val = int(num1[i]) * int(num2[j]) + res[i+j+1]  # 加上原个位位置可能存在的数值
                res[i+j] += sum_val / 10  # 取十位, 同时加上该位置原来可能存在的值
                res[i+j+1] = sum_val % 10   # 取个位
        for i in range(len(res)):
            if res[i] != 0:
                return ''.join([str(num) for num in res[i:]])

