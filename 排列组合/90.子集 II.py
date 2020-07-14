#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/subsets-ii/

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res = []
        def traceback(candidate, chosen_path):
            res.append(chosen_path[:])
            for i in range(len(candidate)):
                num = candidate[i]
                if i > 0 and candidate[i] == candidate[i-1]:    # 剪掉重复元素路径
                    continue
                if chosen_path and chosen_path[-1] > num:
                    continue
                candidate.remove(num)
                chosen_path.append(num)
                print chosen_path, num
                traceback(candidate, chosen_path)
                candidate.insert(i, num)
                chosen_path.pop()
        traceback(nums, [])
        return res

nums = [1,2,2]
print Solution().subsetsWithDup(nums)