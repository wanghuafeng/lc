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
        str_dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in str_dic:
                str_dic[key].append(s)
            else:
                str_dic[key] = [s]
        return str_dic.values()