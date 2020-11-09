#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/
(递归)

当我们用递归去做这个题时不要被题目误导，应该要明确一点
这个函数的功能有三个：
    给定两个节点 p 和 q
    1.如果 p 和 q 都存在，则返回它们的公共祖先；
    2.如果只存在一个，则返回存在的一个；
    3.如果 p 和 q 都不存在，则返回NULL

本题说给定的两个节点都存在，那自然还是能用上面的函数来解决
具体思路：
    （1） 如果当前结点 root 等于 NULL，则直接返回 NULL
    （2） 如果 root 等于 p 或者 q ，那这棵树一定返回 p 或者 q
    （3） 然后递归左右子树，因为是递归，使用函数后可认为左右子树已经算出结果，用 left 和 right 表示
    （4） 此时若left为空，那最终结果只要看 right；若 right 为空，那最终结果只要看 left
    （5） 如果 left 和 right 都非空，因为只给了 p 和 q 两个结点，都非空，说明一边一个，因此 root 是他们的最近公共祖先
    （6） 如果 left 和 right 都为空，则返回空（其实已经包含在前面的情况中了）

时间复杂度是O(n)：每个结点最多遍历一次或用主定理，空间复杂度是 O(n)：需要系统栈空间

https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/c-jing-dian-di-gui-si-lu-fei-chang-hao-li-jie-shi-/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root