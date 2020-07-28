#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/pascals-triangle/

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
    输入: 5
输出:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        res = [[1]]
        for num in range(1, numRows):
            tmp = [1]
            last_item = res[-1]
            for i in range(len(last_item)-1):
                val = last_item[i] + last_item[i+1]
                tmp.append(val)
            tmp.append(1)
            res.append(tmp)
        return res

print Solution().generate(6)
