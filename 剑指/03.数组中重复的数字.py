#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
    输入：
        [2, 3, 1, 0, 2, 5, 3]
    输出：
        2 或 3
限制：
    2 <= n <= 100000

注:
    Python 中， a, b = c, d操作的原理是先暂存元组 (c, d)
    然后 “按左右顺序” 赋值给 a 和 b 。
    因此，若写为nums[i], nums[nums[i]] = nums[nums[i]], nums[i],
    则 nums[i] 会先被赋值，之后 nums[nums[i]] 指向的元素则会出错。
"""

class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        char_set = set()
        for num in nums:
            if num in char_set:
                return num
            char_set.add(num)



class Solution(object):
    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]
        return nums

    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[nums[i]], nums[i]  = nums[i], nums[nums[i]]
            self.swap(nums, nums[i], nums[nums[i]])
        return -1

nums = [2, 3, 1, 0, 2, 5, 3]
print(Solution().findRepeatNumber(nums))