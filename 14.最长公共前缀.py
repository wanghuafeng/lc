#!-*- coding:utf-8 -*-
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        first_s = strs[0]
        min_len = len(strs[0])
        for s in strs:
            min_len = min(min_len, len(s))
        for i in range(min_len):
            char = first_s[i]
            for s in strs[1:]:
                if s[i] != char:
                    return first_s[:i]  # 若中途有不相等的，直接返回
        return first_s[:min_len]    # 所有字符都相同，则截取当前最小字符串长度部分