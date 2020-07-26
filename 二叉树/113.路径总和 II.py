#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/path-sum-ii/

给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。
示例:
    给定如下二叉树，以及目标和 sum = 22，
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1
返回:
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        def helper(root, partial_sum, chosen_path):
            if not root:
                return
            if not root.left and not root.right and partial_sum == root.val:
                chosen_path.append(root.val)
                res.append(chosen_path[:])
            helper(root.left, partial_sum-root.val, chosen_path+[root.val])
            helper(root.right, partial_sum-root.val, chosen_path+[root.val])
        helper(root, sum, [])
        return res
