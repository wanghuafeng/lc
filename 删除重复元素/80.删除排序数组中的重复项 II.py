#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。


示例 1:
    给定 nums = [1,1,1,2,2,3],
    函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
    你不需要考虑数组中超出新长度后面的元素。

示例 2:
    给定 nums = [0,0,1,1,1,1,2,3,3],
    函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
    你不需要考虑数组中超出新长度后面的元素。

    题目中规定每个元素最多出现两次，因此，应检查快指针指向的元素和慢指针指针所指向单元的前一个元素是否相等。
    相等则不更新慢指针，只更新快指针；不相等时，先将慢指针后移一位，再将快指针指向的元素覆写入慢指针指向的单元，
    最后更新快指针。
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        if num_len <= 2:
            return num_len
        left = 1
        for i in range(2, num_len):
            if nums[i] != nums[left-1]:
                left += 1
                nums[left] = nums[i]
        return left + 1
nums= [0,0,1,1,1,1,2,3,3]
print Solution().removeDuplicates(nums)