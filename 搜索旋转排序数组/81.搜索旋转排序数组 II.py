#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:
    输入: nums = [2,5,6,0,0,1,2], target = 0
    输出: true
示例 2:
    输入: nums = [2,5,6,0,0,1,2], target = 3
    输出: false

进阶:
    这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
    这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]: # 较33题添加额外逻辑，去除连续相等数字影响
                left += 1
                continue
            if nums[left] <= nums[mid]:   # 左侧有序    (闭区间)
                if nums[left] <= target and target < nums[mid]:  # target在左侧，注意边界问题
                    right = mid - 1
                else:
                    left = mid + 1
            else:    # 右侧有序
                if nums[mid] < target and target <= nums[right]: # target在右侧，注意边界问题
                    left = mid + 1
                else:
                    right = mid - 1
        return False


nums = [1,1,0,0,1,1]
target = 2
nums = [1,1,3,1]
target = 3
# nums = [1,3]
# target = 2
print Solution().search(nums, target)