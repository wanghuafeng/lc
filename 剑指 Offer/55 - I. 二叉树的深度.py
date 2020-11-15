#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
    给定二叉树 [3,9,20,null,null,15,7]，

        3
       / \
      9  20
        /  \
       15   7
    返回它的最大深度 3 。
提示：
    节点总数 <= 10000
    注意：本题与主站 104 题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

解题思路:
    https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/solution/mian-shi-ti-55-i-er-cha-shu-de-shen-du-xian-xu-bia/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        DFS
        """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        层序遍历
        """
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            res += 1
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
        return res