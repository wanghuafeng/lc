#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
    输入: nums = [4,5,6,7,0,1,2], target = 0
    输出: 4
示例 2:
    输入: nums = [4,5,6,7,0,1,2], target = 3
    输出: -1

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:   # 左侧有序    (闭区间)
                if nums[left] <= target and target < nums[mid]:  # target在左侧，注意边界问题
                    right = mid - 1
                else:
                    left = mid + 1
            else:    # 右侧有序
                if nums[mid] < target and target <= nums[right]: # target在右侧，注意边界问题
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

nums = [1,3]
target = 2
print Solution().search(nums, target)