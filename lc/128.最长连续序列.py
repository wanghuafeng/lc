#!-*- coding:utf-8 -*-
"""给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
	输入：nums = [100,4,200,1,3,2]
	输出：4
	解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
	输入：nums = [0,3,7,2,5,8,4,6,0,1]
	输出：9

示例 3：
	输入：nums = [1,0,1,2]
	输出：3

提示：
	0 <= nums.length <= 105
	-109 <= nums[i] <= 109
"""

class Solution(object):
	# 思路1：排序+去重
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
        	return length
        mem_hash = {0:1} # key:index; value: 至index元素最大序列长
        sorted_nums = sorted(set(nums))
        for i in range(1, len(sorted_nums)):
        	num = sorted_nums[i]
        	if num == sorted_nums[i-1]+1:
        		mem_hash[i] = mem_hash[i-1]+1
        	else:
        		mem_hash[i] = 1
        return max(mem_hash.values())

class Solution(object):
	# 1.筛选出区间起始元素
	# 2.最小元素自增，判断是否在hash列表中，使区间长度自增
	# 3.当前最大长度与区间长度取最大值
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        nums_set = set(nums)
        for num in nums_set:
        	if num - 1 in nums_set:	# 只关注区间起始元素
        		continue
        	# 区间最小元素开始
        	curr_len = 1
        	while num + 1 in nums_set:
        		curr_len += 1
        		num += 1
        	max_len = max(curr_len, max_len)
        return max_len



nums =  [100,4,200,1,3,2]
print(Solution().longestConsecutive(nums))



















