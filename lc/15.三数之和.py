#!-*- coding:utf-8 -*-
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length):
            if nums[i] > 0: # 如果当前数字大于0，则三数之和一定大于0，所以结束循环
                return res

            if i > 0 and nums[i] == nums[i-1]:  # 去重
                continue

            left = i + 1
            right = length - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1   # 去重
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1  # 去重
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return res