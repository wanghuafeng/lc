#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/reverse-linked-list-ii/

反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
    1 ≤ m ≤ n ≤ 链表长度。

示例:

    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL

思路:
    找到要翻转部分的链表,将其翻转,再与原链表拼接;
"""
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        dummy_head.next = head
        node = dummy_head
        for i in range(m-1):
            node = node.next

        prev = None
        curr = node.next
        for i in range(n-m+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        node.next.next = curr
        node.next = prev
        return dummy_head.next