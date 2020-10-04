#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
    输入：
        ["CQueue","appendTail","deleteHead","deleteHead"]
        [[],[3],[],[]]
    输出：[null,null,3,-1]
示例 2：
    输入：
        ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
        [[],[],[5],[2],[],[]]
    输出：[null,-1,null,null,5,2]

提示：
    1 <= values <= 10000
    最多会对 appendTail、deleteHead 进行 10000 次调用

"""

class CQueue(object):

    def __init__(self):
        self.in_stack = []  # 只负责入栈
        self.out_stack = [] # 只负责出栈

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.in_stack.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        if self.out_stack:  # 如果出栈队列有元素，则直接返回
            return self.out_stack.pop()
        if not self.in_stack:  # 如果出栈队列没有元素，入栈队列也没有元素，则直接返回-1
            return -1
        while self.in_stack:    # 如果出栈队列没有元素，出栈队列中有元素
            self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()