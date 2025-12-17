#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：
    输入：[3,4,5,1,2]
    输出：1

示例 2：
    输入：[2,2,2,0,1]
    输出：0
"""
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = left + (right-left)/2
            if numbers[mid] < numbers[right]:   # 轴在左侧
                right = mid
            elif numbers[mid] > numbers[right]: # 轴在右侧
                left = mid + 1
            else:   # 若相等，则去重
                right -= 1
        return numbers[right]


nums = [3,4,5,1,2]
print(Solution().minArray(nums))