#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
给定一个二叉树，原地将它展开为一个单链表。

例如，给定二叉树
        1
       / \
      2   5
     / \   \
    3   4   6
将其展开为：
    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6

解题思路：
    其实是分为三步：
        1.首先将根节点的左子树变成链表
        2.其次将根节点的右子树变成链表
        3.最后将变成链表的右子树放在变成链表的左子树的最右边

        这就是一个递归的过程，递归的一个非常重要的点就是：
            不去管函数的内部细节是如何处理的，我们只看其函数作用以及输入与输出。
        对于函数flatten来说：
            函数作用：将一个二叉树，原地将它展开为链表
            输入：树的根节点
            输出：无
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        tmp_right = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp_right