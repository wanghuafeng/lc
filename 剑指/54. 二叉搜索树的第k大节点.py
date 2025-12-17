#!-*- coding:utf-8 -*-
"""
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:

    输入: root = [3,1,4,null,2], k = 1
       3
      / \
     1   4
      \
       2
    输出: 4

示例 2:
    输入: root = [5,3,6,2,4,null,null,1], k = 3
           5
          / \
         3   6
        / \
       2   4
      /
     1
    输出: 4
     
限制：
    1 ≤ k ≤ 二叉搜索树元素个数

解题思路:
    https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/mian-shi-ti-54-er-cha-sou-suo-shu-de-di-k-da-jie-d/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [(0, root)]
        cnt = 0
        while stack:
            status, node = stack.pop()
            if not node:
                continue
            if status == 1: # 已访问过
                cnt += 1
                if cnt == k:
                    return node.val
            else:   # 未被访问过
                stack.append((0, node.left))
                stack.append((1, node))
                stack.append((0, node.right))


class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cnt = 0
        self.res = None
        def helper(node):
            if not node:
                return
            helper(node.right)
            self.cnt += 1
            if self.cnt == k:
                self.res = node.val
                return
            helper(node.left)
        helper(root)
        return self.res