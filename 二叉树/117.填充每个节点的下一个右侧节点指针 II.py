#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/

给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
 
进阶：
    你只能使用常量级额外空间。
    使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 
示例：
    输入：root = [1,2,3,4,5,null,7]
    输出：[1,#,2,3,#,4,5,7,#]
    解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。

提示：
    树中的节点数小于 6000
    -100 <= node.val <= 100

    // 先确保 root.right 下的节点的已完全连接，因 root.left 下的节点的连接
    // 需要 root.left.next 下的节点的信息，若 root.right 下的节点未完全连
    // 接（即先对 root.left 递归），则 root.left.next 下的信息链不完整，将
    // 返回错误的信息。可能出现的错误情况如下图所示。此时，底层最左边节点将无
    // 法获得正确的 next 信息：
    //                  o root
    //                 / \
    //     root.left  o —— o  root.right
    //               /    / \
    //              o —— o   o
    //             /        / \
    //            o        o   o
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        [2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]
"""

class Solution(object):
    def get_next_node(self, node):
        while node:
            if node.left:
                return node.left
            elif node.right:
                return  node.right
            else:
                node = node.next
        return None


    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = self.get_next_node(root.next)
        if root.right:
            root.right.next = self.get_next_node(root.next)
        self.connect(root.right)
        self.connect(root.left)
        return root