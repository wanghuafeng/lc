#!-*- coding:utf-8 -*-

"""
https://leetcode-cn.com/problems/longest-valid-parentheses/

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
示例 1:
    输入: "(()"
    输出: 2
    解释: 最长有效括号子串为 "()"
示例 2:
    输入: ")()())"
    输出: 4
    解释: 最长有效括号子串为 "()()"


 思路1: 栈
1、栈底永远保存着当前有效子串的前一个字符的下标，初始化: 将-1放入栈中。
2、遇到左括号就入栈；
3、遇到右括号就将栈顶元素出栈。此时有两种情况：
    3.1 如果栈顶元素出栈后，栈内剩下的元素不为空，则说明弹出的这个栈顶元素一定是左括号，因为栈底有保险。
    3.2 如果栈顶元素出栈后，栈内为空，则说明刚刚弹出的这个栈顶元素就是之前的“有效子串前一位的字符下标”，所以此时应该使用当前的右括号的下标入栈，更新这个“有效子串前一位的字符下标”。

"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:   # 栈内元素为空
                    stack.append(i)
                max_len = max(max_len, i-stack[-1])
        return max_len


if __name__ == "__main__":
    s = ')()())'
    print Solution().longestValidParentheses(s)
