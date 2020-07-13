#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/partition-list/

给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        small = ListNode(-1)
        small_head = small
        bigger = ListNode(-1)
        bigger_head = bigger
        while head:
            curr_val = head.val
            if curr_val < x:
                small.next = ListNode(curr_val)
                small = small.next
            else:
                bigger.next = ListNode(curr_val)
                bigger = bigger.next
            head = head.next
        small.next = bigger_head.next
        return small_head.next

