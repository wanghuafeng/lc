#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。

示例:
    给定有序数组: [-10,-3,0,5,9],

    一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
          0
         / \
       -3   9
       /   /
     -10  5
解题思路:
    1.递归    (注意边界控制)
    2.迭代
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        def dfs(nums, start, end):
            if start > end:   # 注意这里的边界控制
                return None
            mid = (start + end) / 2
            root = TreeNode(nums[mid])
            root.left = dfs(nums, start, mid-1)
            root.right = dfs(nums, mid+1, end)
            return root
        return dfs(nums, 0, len(nums)-1)

