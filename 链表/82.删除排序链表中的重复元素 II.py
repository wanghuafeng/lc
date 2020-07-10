#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/

给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
示例 1:
    输入: 1->2->3->3->4->4->5
    输出: 1->2->5
示例 2:
    输入: 1->1->1->2->3
    输出: 2->3


解题思路:
        如果是这种情况
             1 --> 1 --> 1 --> 2 --> 3
             head  next
        1.则需要移动next直到出现与当前head.value不相等的情况（含null）
        2.并且此时的head已经不能要了，因为已经head是重复的节点
        --------------else-------------
             1 --> 2 --> 3
             head  next
        3.如果没有出现1的情况，则递归返回的节点就作为head的子节点
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        if head.val == head.next.val:   # 有重复元素
            while head.next and  head.val == head.next.val:
                head.next = head.next.next
            head = self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head

