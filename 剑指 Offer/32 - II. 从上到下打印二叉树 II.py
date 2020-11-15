#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
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
          [9,20],
          [15,7]
        ]
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
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
            if len(res)-1 != level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
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
            tmp = []
            level_tmp = []  # 借助辅助变量
            for node in queue:
                level_tmp.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(level_tmp)
            queue = tmp
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
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res

