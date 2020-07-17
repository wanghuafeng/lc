#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/unique-binary-search-trees/
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
    给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3


动态规划分析
在已知前n-1个数的二叉搜索树数目后，插入第n个数，有哪些情况？
1.第n个数做根节点，前n-1个数形成其左子树，右子树为0个数，dp[n-1]*dp[0]种
2.第n-1个数做根节点，左子树为前n-2个数，右子树为第n个数，dp[n-2]*dp[1]种
...
n-i+1.第i个数做根节点，左子树为前i-1个数，右子树为后n-i个数，dp[i-1]*dp[n-i]种
...
n.第1个数做根节点，左子树为0个数，右子树为后n-1个数，dp[0]*dp[n-1]种
我们将所有情况的二叉搜索树加起来即可
技巧：不妨初始化dp[0]=1,则可顺利循环解决

"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二叉搜索数的特征，左子树小于根，右子树大于根
        dp = [0 for i in range(n+1)]
        dp[0] = 1   # dp[0]初始化为1
        for i in range(1, n+1):   # 从1...n的二叉搜索数数目
            for j in range(1, i+1):  # 逐步选用1...n作为根节点
                dp[i] += dp[j-1]*dp[i-j]    # 左侧j-1个数，右侧i-j个数
        return dp[n]
