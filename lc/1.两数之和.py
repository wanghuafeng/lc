#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/two-sum/
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

示例 1：
    输入：nums = [2,7,11,15], target = 9
    输出：[0,1]
    解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
    输入：nums = [3,2,4], target = 6
    输出：[1,2]

示例 3：
    输入：nums = [3,3], target = 6
    输出：[0,1]


进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for i in range(len(nums)): 
            if nums[i] in mapping:
                return [mapping[nums[i]], i]
            else:
                var = target - nums[i]
                mapping[var] = i

nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))


"""
    思路：遍历给定数组，能匹配的数字放到mapping中，遍历到的index元素去mapping中查找，也即查看[0, index-1]中 是否index元素匹配得元素
"""


