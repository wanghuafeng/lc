#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/combination-sum/

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。 

示例 1:
    输入: candidates = [2,3,6,7], target = 7,
    所求解集为:
    [
      [7],
      [2,2,3]
    ]

示例 2:
    输入: candidates = [2,3,5], target = 8,
    所求解集为:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]

思路
直接上回溯算法框架。解决一个回溯问题，实际上就是一个决策树的遍历过程。你只需要思考 3 个问题：
    1、路径：也就是已经做出的选择。
    2、选择列表：也就是你当前可以做的选择。
    3、结束条件：也就是到达决策树底层，无法再做选择的条件。

代码方面，回溯算法的框架：
    result = []
    def backtrack(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」

"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def traceback(partial_candidates, sum_val, chosen_path):
            if sum_val == target:   # 路径满足条件
                res.append(chosen_path[:])  # python为引用传递，所以这里用拷贝方式添加
                return
            elif sum_val > target:  # 结果大于目标值直接返回
                return
            for item in partial_candidates:
                if chosen_path:
                    if chosen_path[-1] > item:  # 选择列表中已排序，如果路径中，最后一个元素小于当前元素，则说明该路径已经被加入过，跳过
                        continue
                chosen_path.append(item)
                traceback(partial_candidates, sum_val+item, chosen_path)
                chosen_path.pop()
        traceback(candidates, 0, [])
        return res

candidates = [2,3,6,7,8]
target = 7
print Solution().combinationSum(candidates, target)


