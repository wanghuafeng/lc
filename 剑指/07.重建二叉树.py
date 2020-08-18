#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 
限制：
    0 <= 节点个数 <= 5000
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        n = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:n+1], inorder[:n])
        root.right = self.buildTree(preorder[n+1:], inorder[n+1:])
        return root