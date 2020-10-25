#!-*- coding:utf-8 -*-
"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
例如输入：
         4
       /   \
      2     7
     / \   / \
    1   3 6   9

镜像输出：
         4
       /   \
      7     2
     / \   / \
    9   6 3   1

示例 1：
    输入：root = [4,2,7,1,3,6,9]
    输出：[4,7,2,9,6,3,1]

限制：
    0 <= 节点个数 <= 1000

注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        递归版本
        """
        if not root:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root


class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        迭代
        """
        stack = [(0, root)]
        while stack:
            status, node = stack.pop()
            if not node:
                continue
            if status == 0:
                stack.append((0, node.left))
                stack.append((1, node))
                stack.append((0, node.right))
            else:
                tmp = node.left
                node.left = node.right
                node.right = tmp
        return root

