#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的
min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。


示例:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.min();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.min();   --> 返回 -2.
 
提示：
    各函数的调用总次数不超过 20000 次
 
注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)
        if not self.B:
            self.B.append(x)
        else:
            if self.B[-1] >= x:
                self.B.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if not self.A:
            return
        v = self.A.pop()
        if v == self.B[-1]:
            self.B.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.A:
            return self.A[-1]

    def min(self):
        """
        :rtype: int
        """
        if self.B:
            return self.B[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()