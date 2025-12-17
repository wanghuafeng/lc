#!-*- coding:utf-8 -*-
"""

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
        1
       / \
      2   2
     / \ / \
    3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
        1
       / \
      2   2
       \   \
       3    3

示例 1：
    输入：root = [1,2,2,3,4,4,3]
    输出：true
示例 2：
    输入：root = [1,2,2,null,3,null,3]
    输出：false

限制：
    0 <= 节点个数 <= 1000
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left and right:   # 左右结点不为空
            if left.val == right.val:   # 左右结点相同
                return self.check(left.left, right.right) and self.check(left.right, right.left)
            else:            # 左右结点不同
                return False
        if not left and not right:  # 左右结点同时为空
            return True
        else:                # 一个为空一个不为空
            return False