#!-*- coding:utf-8 -*-

"""
https://leetcode-cn.com/problems/wildcard-matching/

给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例 1:
    输入:
        s = "aa"
        p = "a"
    输出: false
    解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:
    输入:
        s = "aa"
        p = "*"
    输出: true
    解释: '*' 可以匹配任意字符串。

解题思路:
    定义dp[s.size()+1][p.size()+1].这样可以处理串为空的情况。
    dp[i][j]表示s[i-1]和p[j-1]（包括这两点）以及之前的字符串能否匹配。

    状态 dp[i][j] : 表示 s 的前 i 个字符和 p 的前 j 个字符是否匹配 (true 的话表示匹配)
    状态转移方程：
        1. 当 s[i] == p[j]，或者 p[j] == ? 那么 dp[i][j] = dp[i - 1][j - 1];
        2. 当 p[j] == * 那么 dp[i][j] = dp[i][j - 1] || dp[i - 1][j]
            其中：
                dp[i][j - 1] 表示 * 代表的是空字符，例如 ab, ab*
                dp[i - 1][j] 表示 * 代表的是非空字符，例如 abcd, ab*
    初始化：
        1. dp[0][0] 表示什么都没有，其值为 true
        2. 第一行 dp[0][j]，换句话说，s 为空，与 p 匹配，所以只要 p 开始为 * 才为 true
        3. 第一列 dp[i][0]，当然全部为 false

        初始dp[0][0]为1。因为两个空串匹配。
        初始化dp[0][i]。表示当s为空串时，p是否全是*。
        dp[0][i]=dp[0][i-1] and p[i-1]=='*';
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]    # 注意二维数组的行列设置

        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] in (s[i-1], "?"):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[m][n]
