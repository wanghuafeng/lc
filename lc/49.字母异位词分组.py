#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/group-anagrams/
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_mapping = {}
        for str in strs:
            sort_str = ''.join(sorted(str))
            if sort_str in hash_mapping:
                hash_mapping[sort_str].append(str)
            else:
                hash_mapping[sort_str] = [str]
        return hash_mapping.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))

"""
    先对数组中的字符串进行排序，排序后进行比对。注意：sorted()对字符串进行排序时，返回的是一个数组，需要做拼接成字符串
"""