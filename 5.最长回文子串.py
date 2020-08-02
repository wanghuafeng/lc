#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/longest-palindromic-substring/
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。
示例 2：
    输入: "cbbd"
    输出: "bb"

解题思路:
    1.暴力法(sorry 超时)
    2.动态规划
        如果一个字符串的头尾两个字符都不相等，那么这个字符串一定不是回文串；
        如果一个字符串的头尾两个字符相等，才有必要继续判断下去。
            如果里面的子串是回文，整体就是回文串；
            如果里面的子串不是回文串，整体就不是回文串。
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        length = len(s)
        max_len = 0
        res = s[0]
        for i in range(length):
            for j in range(i+1, length):
                partial_str = s[i:j+1]
                if self.check_valid(partial_str):
                    if max_len < j-i+1:
                        res = partial_str
                        max_len = j-i+1
        return res

    def check_valid(self, paitial_str):
        start = 0
        end = len(paitial_str) - 1
        while start < end:
            if not paitial_str[start] == paitial_str[end]:
                return False
            start += 1
            end -= 1
        return True


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        length = len(s)
        max_len = 0
        res = ''
        dp = [[False]*length for _ in range(length)]
        for j in range(length):
            for i in range(j+1):
                if s[i] == s[j]:
                    if j - i + 1 < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and max_len < j - i + 1:
                    max_len = j - i + 1
                    res = s[i: j+1]
        return res


s = 'cbbd'
s = "ac"
# s = 'babad'
print Solution().longestPalindrome(s)