#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: [3,4]
示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: [-1,-1]


二分查找的边界问题:
    https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/
"""

class Solution(object):
    def left_bound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = right - (right - left) / 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def right_bound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = right - (right - left) / 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right <= -1 or nums[right] != target:
            return -1
        return right

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        return [self.left_bound(nums, target), self.right_bound(nums, target)]