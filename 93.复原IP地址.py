#!-*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/restore-ip-addresses/

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

示例:
    输入: "25525511135"
    输出: ["255.255.11.135", "255.255.111.35"]


解题思路:(https://leetcode-cn.com/problems/restore-ip-addresses/solution/2020041693medianhui-su-di-gui-fu-yuan-ip-di-zhi-by/)
首先创建 ans 来接收复原后的所有 ip 地址，然后通过创建回溯方法进行筛选，最终返回 ans。

创建回溯方法体需要传入四个参数进行把控：
    1.给定的数字字符串 s，
    2.回溯过程中遍历到的位置 pos，
    3.当前确定好的 ip 段的数量，
    4.收集结果的 ans
考虑方法体出口：
    如果确定好 4 段并且遍历完整个 s,就将 cur 之间的段以 . 分隔开来放入 ans

接下来对 s 进行筛选,其中注意每段的长度最大为 3,拆箱为 int 后的长度不超过 255,起始位置不能为 0
控制好这些边界条件后就可以就可以正常的利用递归和回溯遍历字符串
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        n = len(s)
        if n < 4 or n > 12: # 字符串的长度小于 4 或者大于 12
            return []
        def traceback(chosen_path, pos):
            if len(chosen_path) == 4 and pos == n:
                res.append('.'.join(chosen_path))
                return
            for i in range(1, 4):
                if pos+i > n:
                    break
                segment = s[pos:pos+i]
                int_seg = int(segment)
                if int_seg > 255:   #  剪枝: 不能大于255
                    continue
                if segment.startswith('0') and len(segment) > 1:    # 剪枝: 段的起始位置不能为 0
                    continue
                chosen_path.append(segment)
                traceback(chosen_path, pos+i)
                chosen_path.pop()
        traceback([], 0)
        return res

s = "25525511135"
print Solution().restoreIpAddresses(s)