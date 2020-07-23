#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/balanced-binary-tree/
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:
    给定二叉树 [3,9,20,null,null,15,7]
        3
       / \
      9  20
        /  \
       15   7
    返回 true 。
示例 2:
    给定二叉树 [1,2,2,3,3,null,null,4,4]

           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    返回 false 。

解题思路: 判断左右字数高度相差是否大于1
    递归
        1.自顶向下方法
        2.自底向上
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def helper(self, node):
        if not node:
            return 0
        left_depth = self.helper(node.left)
        right_depth = self.helper(node.right)
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_depth = self.helper(root.left)
        right_depth = self.helper(root.right)
        return abs(left_depth-right_depth)<2 and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return 0
        left_depth = self.helper(node.left) + 1
        right_depth = self.helper(node.right) + 1
        if abs(left_depth-right_depth) > 1:
            self.res = False
        return max(left_depth, right_depth)