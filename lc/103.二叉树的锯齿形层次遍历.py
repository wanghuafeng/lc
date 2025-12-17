#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
    给定二叉树 [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回锯齿形层次遍历如下：

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

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        def bfs(node, level):
            if not node:
                return
            if len(res) == level:
                res.append([])
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
            bfs(node.left, level+1)
            bfs(node.right, level+1)
        bfs(root, 0)
        return res


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        l2r = True
        while queue:
            tmp_queue = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if not node:
                    continue
                if l2r: # 从左至右入栈
                    tmp_queue.append(node.val)
                else:   # 从右至左入栈
                    tmp_queue.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            l2r = not l2r   # 一层遍历完毕，调整方向
            res.append(tmp_queue)
        return res