#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/add-two-numbers/
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        dummy_head = ListNode(-1)
        curr_node = dummy_head
        plus_val = 0
        while l1 or l2:
            if l1 and l2:
                sum_val = l1.val + l2.val + plus_val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum_val = l1.val + plus_val
                l1 = l1.next
            else:
                sum_val = l2.val + plus_val
                l2 = l2.next
            # 处理进位
            if sum_val >= 10:
                plus_val = 1
            else:
                plus_val = 0
            # 节点值对10取余
            sum_val = sum_val % 10
            curr_node.next = ListNode(sum_val)
            curr_node = curr_node.next

        # 处理最高位有进位的问题
        if plus_val == 1:
            curr_node.next = ListNode(plus_val)
        return dummy_head.next