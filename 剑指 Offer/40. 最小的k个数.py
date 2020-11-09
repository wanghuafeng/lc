#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
输入整数数组 arr ，找出其中最小的 k 个数。
例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
    输入：arr = [3,2,1], k = 2
    输出：[1,2] 或者 [2,1]

示例 2：
    输入：arr = [0,1,2,1], k = 1
    输出：[0]
限制：
    0 <= k <= arr.length <= 10000
    0 <= arr[i] <= 10000
"""

import heapq
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not arr or k == 0:
            return []
        hp = []
        heapq.heapify(hp)
        for num in arr:
            if len(hp) >= k: # 超过了限定元素个数
                if -hp[0] > num:   # 当前元素比队列中所有元素都小
                    heapq.heappush(hp, -num)
                    heapq.heappop(hp)
            else:   # 未达到k个元素，则直接添加
                heapq.heappush(hp, -num)
        return [-num for num in hp]


class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        快排思想
        """
        if not arr or k == 0:
            return []
        self.k = k-1    # k==len(arr)-1时会溢出
        return self.quick_sort(arr, 0, len(arr)-1)

    def quick_sort(self, arr, l, r):
        p = self.partition(arr, l, r)
        if p == self.k:
            return arr[:self.k+1]
        if p > self.k:
            return self.quick_sort(arr, l, p-1)
        else:
            return self.quick_sort(arr, p+1, r)

    def partition(self, nums, left, right):
        point_val = nums[left]
        while left < right:
            while left < right and nums[right] >= point_val:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= point_val:
                left += 1
            nums[right] = nums[left]
        nums[left] = point_val
        return left


l = [4, 5, 1, 6, 2, 7, 3, 8]
l = [0,0,2,3,2,1,1,2,0,4]
t = 10
print Solution().getLeastNumbers(l, t)
