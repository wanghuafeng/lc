#!-*- coding:utf-8 -*-
"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
示例1：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
限制：
    0 <= 链表长度 <= 1000
注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        combine_l = ListNode(-1)
        curr = combine_l
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return combine_l.next