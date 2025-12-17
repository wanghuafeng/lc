#!-*- coding:utf-8 -*-


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        res = ["" for _ in range(numRows)]
        flag = -1
        slot = 0
        for char in s:
            res[slot] += char
            if slot == numRows-1 or slot == 0:
                flag = - flag
            slot += flag
            print slot
        return ''.join(res)
s = "AB"
numRows = 1
# s = "PAYPALISHIRING"
# numRows = 3
print Solution().convert(s, numRows)