#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/combination-sum-ii/

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：
    所有数字（包括目标数）都是正整数。
    解集不能包含重复的组合。 

示例 1:
    输入: candidates = [10,1,2,7,6,1,5], target = 8,
    所求解集为:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]

示例 2:
    输入: candidates = [2,5,2,1,2], target = 5,
    所求解集为:
    [
      [1,2,2],
      [5]
    ]


去重思路:
    这个方法最重要的作用是，可以让同一层级，不出现相同的元素。即
    例1:
          1
         / \
        2   2  这种情况不会发生 但是却允许了不同层级之间的重复即：
       /     \
      5       5

    例2:
          1
         /
        2      这种情况确是允许的
       /
      2

"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def traceback(candidates, sum_val, trace):
            if sum_val > target:
                return
            elif sum_val == target:
                res.append(trace[:])
                return
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:  # 过滤当前层级的重复元素
                    continue
                trace.append(candidates[i])
                traceback(candidates[i+1:], sum_val+candidates[i], trace)
                trace.pop()
        traceback(candidates, 0, [])
        return res
