#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/first-missing-positive/

给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

示例 1:
    输入: [1,2,0]
    输出: 3

示例 2:
    输入: [3,4,-1,1]
    输出: 2

示例 3:
    输入: [7,8,9,11,12]
    输出: 1

提示：
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。


解题思路:
    就把 11 这个数放到下标为 00 的位置， 22 这个数放到下标为 11 的位置，按照这种思路整理一遍数组。然后我们再遍历一次数组，第 11 个遇到的它的值不等于下标的那个数，就是我们要找的缺失的第一个正数。
    那就是数值为 i 的数映射到下标为 i - 1 的位置
"""


class Solution(object):
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            while nums[i] >= 1 and nums[i] <= length and nums[i] != nums[nums[i] - 1]:
               self.swap(nums, i, nums[i] - 1)

        for i in range(length):
            if i != nums[i]-1:
                return i+1
        return length+1