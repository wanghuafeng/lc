#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
    输入：s = "We are happy."
    输出："We%20are%20happy."
限制：
    0 <= s 的长度 <= 10000
"""

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for char in s:
            if char == ' ':
               res.append('%20')
            else:
                res.append(char)
        return ''.join(res)

s = " 1  "
print(s.split())
print(Solution().replaceSpace(s))