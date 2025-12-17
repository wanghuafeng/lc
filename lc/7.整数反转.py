#!-*- coding:utf-8 -*-
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        val = x if x >= 0 else -x
        new_val = str(val)[::-1]
        int_val = int(new_val)
        if -2**31 < int_val < 2**31-1:
            return int_val if x > 0 else -int_val
        return 0


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            x = -x
            flag = -1
        reverse_x = 0
        while x > 0:
            reverse_x = reverse_x * 10 + x % 10
            x //= 10
        if reverse_x < - 2**31 or reverse_x > 2**31 - 1:
            return 0
        return reverse_x if flag > 0 else -reverse_x

x = -123
print(Solution().reverse(x))
