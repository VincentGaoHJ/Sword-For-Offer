# coding=utf-8
"""
@Time   : 2020/10/22  10:41 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 38. 字符串的排列
    https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
"""


class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = list(s)
        s.sort()
        s = ''.join(s)

        n = len(s)
        res = []

        def dfs(s, tmp, n):
            if len(tmp) == n:
                res.append(tmp)
                return
            for i in range(len(s)):
                if i > 0 and s[i] == s[i - 1]:
                    continue
                dfs(s[i + 1:] + s[:i], tmp + s[i], n)

        dfs(s, '', n)
        return res


def offer_38(s):
    """
    输入一个字符串，打印出该字符串中字符的所有排列。
    你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
    :param s:
    :return:
    """
    solution = Solution()
    output = solution.permutation(s)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 38. 字符串的排列
    offer_38(s="abc")
