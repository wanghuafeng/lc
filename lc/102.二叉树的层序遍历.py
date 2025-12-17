#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
    二叉树：[3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回其层次遍历结果：
    [
      [3],
      [9,20],
      [15,7]
    ]
1.递归
2.迭代
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def bfs(node, level):
            if not node:
                return
            if len(res) == level:   # 新一层时,扩容
                res.append([])
            res[level].append(node.val)
            bfs(node.left, level+1)
            bfs(node.right, level+1)
        bfs(root, 0)
        return res


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            level_queue = []      # 临时变量，记录当前层的节点
            for i in range(len(queue)): # 遍历某一层的节点
                node = queue.pop(0)
                if not node:
                    continue
                level_queue.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_queue)
        return res

