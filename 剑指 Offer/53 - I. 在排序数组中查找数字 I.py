#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
统计一个数字在排序数组中出现的次数。

示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: 2

示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: 0

限制：
    0 <= 数组长度 <= 50000

注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        left_bound = self.left_bound(nums, target)
        if left_bound == -1:
            return 0
        right_bound = self.right_bound(nums, target)
        return right_bound - left_bound + 1


    def left_bound(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end-start)/2
            if nums[mid] == target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if start >= len(nums) or nums[start] != target: # 校验start，以保证不越界
            return -1
        return start

    def right_bound(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end-start)/2
            if nums[mid] == target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if end <= -1 or nums[end] != target:
            return -1
        return end
