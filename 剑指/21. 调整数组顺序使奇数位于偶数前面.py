#!-*- coding:utf-8 -*-
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
    输入：nums = [1,2,3,4]
    输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。


思路:
    1. 左侧指针右移 直到遇到偶数
    2. 右侧指针左移 直到遇到奇数
    3. 交换左右指针元素

"""
class Solution(object):
    def _swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]
        return nums

    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] % 2 != 0: # 偶数
                left += 1
                continue
            elif nums[right] % 2 != 1:   # 奇数
                right -= 1
                continue

            self._swap(nums, left, right)
        return nums

nums = [1,2,3,4]
print Solution().exchange(nums)