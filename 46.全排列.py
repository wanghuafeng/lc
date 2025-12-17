#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/permutations/

给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def traceback(candidate, chosen_path):
            if not candidate:
                res.append(chosen_path[:])
                return
            for i in range(len(candidate)):
                num = candidate[i]
                candidate.remove(num)
                chosen_path.append(num)
                traceback(candidate, chosen_path)
                candidate.insert(i, num)
                chosen_path.remove(num)

        traceback(nums, [])
        return res

class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        num_lenght = len(nums)
        candidate_mark = [False for _ in range(num_lenght)]
        def traceback(chosen_path):
            if len(chosen_path) == num_lenght:
                res.append(chosen_path[:])
                return
            for i in range(num_lenght):
                if candidate_mark[i]:
                    continue
                candidate_mark[i] = True
                chosen_path.append(nums[i])
                traceback(chosen_path)
                candidate_mark[i] = False
                chosen_path.pop()
        traceback([])
        return res
