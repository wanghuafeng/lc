#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1:
    输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
    输出: 2
限制：
    1 <= 数组长度 <= 50000
注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        哈希表统计法
        """
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        ret = nums[0]
        for num in d:
            if d.get(num) > d.get(ret):
                ret = num
        return ret


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        摩尔投票法
        """
        x = nums[0]
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            if num == x:
                votes += 1
            else:
                votes -= 1
        return x


l = [1, 2, 3, 2, 2, 2, 5, 4, 2]
r = Solution().majorityElement(l)
print(r)