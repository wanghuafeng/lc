#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
    输入: 1->1->2
    输出: 1->2

示例 2:
    输入: 1->1->2->3->3
    输出: 1->2->3

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy_head = ListNode(-1)
        dummy_head.next = head
        curr = head
        while curr and curr.next:
            while curr and curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        return dummy_head.next