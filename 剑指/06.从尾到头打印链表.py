#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
    输入：head = [1,3,2]
    输出：[2,3,1]
限制：
    0 <= 链表长度 <= 10000
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        执行用时：16 ms, 在所有 Python 提交中击败了 99.03% 的用户
        内存消耗：16.2 MB , 在所有 Python 提交中击败了76.85% 的用户
        """
        if not head:
            return []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.reverse()
        return res


class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        执行用时：140 ms, 在所有 Python 提交中击败了 7.50% 的用户
        内存消耗：23.3 MB , 在所有 Python 提交中击败了8.99% 的用户
        """
        if not head:
            return []
        return self.reversePrint(head.next) + [head.val]