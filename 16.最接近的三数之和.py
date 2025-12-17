#!-*- coding:utf-8 -*-
"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
    输入：nums = [-1,2,1,-4], target = 1
    输出：2
    解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        res = float('inf')
        for i in range(length):
            left = i + 1
            right = length - 1
            while  left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return target
                elif total < target:
                    left += 1
                else:
                    right -= 1
                if abs(target - total) < abs(target - res):
                    res = total
        return res


nums = [-1,2,1,-4]
target = 1
nums = [0,1,2]
target=3
print Solution().threeSumClosest(nums, target)