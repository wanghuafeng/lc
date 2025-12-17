#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/permutations-ii/

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        res = []
        def traceback(candidate, chosen_list):
            if not candidate:
                res.append(chosen_list[:])
                return
            for i in range(len(candidate)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                num = candidate[i]
                candidate.remove(num)
                chosen_list.append(num)
                traceback(candidate, chosen_list)
                chosen_list.pop()
                candidate.insert(i, num)
        traceback(nums, [])
        return res

class Solution2(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        res = []
        used_list = [False for _ in range(length)]
        def traceback(chosen_list):
            if len(chosen_list) == length:
                res.append(chosen_list[:])
                return
            for i in range(length):
                if used_list[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used_list[i-1]==False:
                    continue
                used_list[i] = True
                chosen_list.append(nums[i])
                traceback(chosen_list)
                used_list[i] = False
                chosen_list.pop()
        traceback([])
        return res