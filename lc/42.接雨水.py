#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/trapping-rain-water/

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        dp_left_max = [0] * length
        left_max = 0
        for i in range(length):
            if i > 0:
                if height[i-1] > left_max:
                    dp_left_max[i] = height[i-1]
                else:
                    dp_left_max[i] = left_max
            left_max = dp_left_max[i]

        dp_right_max = [0] * length
        right_max = 0
        for i in range(length-1, -1, -1):
            if i < length-1:
                if height[i+1] > right_max:
                    dp_right_max[i] = height[i+1]
                else:
                    dp_right_max[i] = right_max
            right_max = dp_right_max[i]

        res = 0
        for i in range(length):
            min_val = min(dp_left_max[i], dp_right_max[i])
            if height[i]>min_val:
                continue
            else:
                res += (min_val-height[i])
        return res

