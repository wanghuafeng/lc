#!-*- coding:utf-8 -*-
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        dev = 1
        while x/dev >= 10:
            dev *= 10
        while x > 10:
            head = x/dev
            tail = x%10
            if head != tail:
                return False
            x = (x%dev)/10  #  输入砍掉首尾数字
            dev /= 100  # 去掉首尾两位数字后，dev需减两位
        return True


x = 121
print Solution().isPalindrome(x)