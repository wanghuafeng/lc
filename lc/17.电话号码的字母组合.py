#!-*- coding:utf-8 -*-
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
    输入："23"
    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        KEY = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        combine_list = KEY.get(digits[0])
        for num in digits[1:]:
            combine_list = self.combine(combine_list, KEY.get(num))
        return combine_list

    def combine(self, l1, l2):
        l = []
        for i in l1:
            for j in l2:
                l.append(i+j)
        return l

digits = "23"
print Solution().letterCombinations(digits)