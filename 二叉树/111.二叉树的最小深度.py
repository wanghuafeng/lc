#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

思路:
    最大深度和最小深度有一个很大的区别，最大深度能够保证最后一个节点绝对是叶子节点，而最小深度不行。
    因为定义说最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
    需要额外加上一个条件， (not root.left or not root.right)
    也就是判断当前节点是不是叶子节点，如果不是返回的值就是不为0的节点+1，如果是叶子结点就是两者较小的结果加1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if not root.left or not root.right:    # 左右子树其中一个为空
            return left_depth+right_depth+1
        else:
            return min(left_depth, right_depth) + 1
