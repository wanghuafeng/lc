#!-*- coding:utf-8 -*-
"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1:
    给定数组 nums = [1,1,2],
    函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
    你不需要考虑数组中超出新长度后面的元素。
示例 2:
    给定 nums = [0,0,1,1,1,2,2,3,3,4],
    函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
    你不需要考虑数组中超出新长度后面的元素。

思路:
    双指针，自左向右移动，遇到不相同的元素时交换到左侧
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        if num_len <= 1:
            return num_len
        left, right = 0, 0
        while right < num_len:
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left+1


nums = [1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,1,2,2,3]
print Solution().removeDuplicates(nums)
