#!-*- coding:utf-8 -*-
"""
思路：
    每次选定围成水槽两板高度 height[left],height[right]中的短板，向中间收窄 1 格
    注意:8块木板，则宽为7，即只考虑相邻间隙距离
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            if height[left] <= height[right]:
                curr_area = height[left] * (right - left)
                left += 1
            else:
                curr_area = height[right] * (right - left)
                right -= 1
            max_area = max(max_area, curr_area)
        return max_area