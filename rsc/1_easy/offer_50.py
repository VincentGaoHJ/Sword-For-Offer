# coding=utf-8
"""
@Time   : 2020/10/25  9:59 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 50. 第一个只出现一次的字符
    https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for c in s:
            dic[c] = c not in dic
        for c in s:
            if dic[c]: return c
        return ' '


def offer_50(s):
    """
    在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
    :param s:
    :return:
    """
    solution = Solution()
    output = solution.firstUniqChar(s)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 50. 第一个只出现一次的字符
    offer_50(s="abaccdeff")
