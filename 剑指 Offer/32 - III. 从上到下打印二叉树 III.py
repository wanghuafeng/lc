#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
    给定二叉树: [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    返回其层次遍历结果：
        [
          [3],
          [20,9],
          [15,7]
        ]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = collections.deque()
        level = 0
        queue.append((root, level))
        while queue:
            node, level = queue.popleft()
            if len(res) - 1 != level:
                res.append([])
            if level % 2 != 0:    # 根据level奇偶性来添加到返回队列中
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
            if node.right:
                queue.append((node.right, level+1))
            if node.left:
                queue.append((node.left, level+1))
        return res