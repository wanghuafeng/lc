#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/pascals-triangle-ii/

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
    输入: 3
    输出: [1,3,3,1]
进阶：
    你可以优化你的算法到 O(k) 空间复杂度吗？
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for num in range(1, rowIndex+1):
            tmp = [1]
            for i in range(len(res)-1):
                val = res[i] + res[i+1]
                tmp.append(val)
            tmp.append(1)
            res = tmp
        return res

print Solution().getRow(3)

