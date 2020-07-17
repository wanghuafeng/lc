#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/

给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

示例：
    输入：3
    输出：
        [
          [1,null,3,2],
          [3,2,null,1],
          [3,1,null,null,2],
          [2,1,3],
          [1,null,2,null,3]
        ]

解释：
    以上的输出对应以下 5 种不同结构的二叉搜索树：

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

提示：
    0 <= n <= 8

解题思路:
    https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/di-gui-zhu-xing-jie-shi-python3-by-zhu_shi_fu/
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        def build_tree(left, right):
            if left > right:
                return [None]
            all_trees = []
            for i in range(left, right+1):
                left_trees = build_tree(left, i-1)
                right_trees = build_tree(i+1, right)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        node = TreeNode(i)
                        node.left = left_tree
                        node.right = right_tree
                        all_trees.append(node)
            return all_trees
        return build_tree(1, n)
