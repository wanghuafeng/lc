#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/validate-binary-search-tree/

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

思路:
    1.中序遍历，升序 (递归)
    2.中序遍历，升序 (迭代)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def dfs(self, node):
        if not node:
            return True
        if not self.dfs(node.left):
            return False
        if node.val <= self.pre_val:
            return False
        self.pre_val = node.val
        return self.dfs(node.right)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.pre_val = float('-inf')
        return self.dfs(root)


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre_val = float('-inf')
        stack = [(0, root)]
        while stack:
            status, node = stack.pop()
            if not node:
                continue
            if status == 0:
                stack.append((0, node.right))
                stack.append((1, node))
                stack.append((0, node.left))
            else:
                if node.val <= pre_val:
                    return False
                pre_val = node.val
        return True
