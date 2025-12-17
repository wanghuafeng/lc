#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
1. 递归算法
2. 迭代
    使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
    如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
    如果遇到的节点为灰色，则将节点的值输出。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        递归算法
        """
        res = []
        def traceback(root):
            if not root:
                return None
            traceback(root.left)
            res.append(root.val)
            traceback(root.right)
        traceback(root)
        return res


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        迭代
        """
        white, grey = 0, 1
        stack = [(white, root)]
        res = []
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == white:
                stack.append((white, node.right))
                stack.append((grey, node.val))
                stack.append((white, node.left))
            else:
                res.append(node)
        return res