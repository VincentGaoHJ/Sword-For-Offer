# coding=utf-8
"""
@Time   : 2020/10/24  11:16 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 48. 最长不含重复字符的子字符串
    https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head, tail = 0, 0
        if len(s) < 2: return len(s)
        res = 1
        while tail < len(s) - 1:
            tail += 1
            if s[tail] not in s[head:tail]:
                res = max(tail - head + 1, res)
            else:
                while s[tail] in s[head:tail]:
                    head += 1
        return res


def offer_(s):
    """
    请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
    :param s:
    :return:
    """
    solution = Solution()
    output = solution.lengthOfLongestSubstring(s)

    print(output)


# 思路：题目中要求答案必须是 子串 的长度，意味着子串内的字符在原字符串中一定是连续的。
# 因此我们可以将答案看作原字符串的一个滑动窗口，并维护窗口内不能有重复字符，同时更新窗口的最大值。
if __name__ == '__main__':
    # 剑指 Offer 48. 最长不含重复字符的子字符串

    # 输出: 3
    # 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    offer_("abcabcbb")

    # 输出: 1
    # 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    offer_("bbbbb")

    # 输出: 3
    # 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
    offer_("pwwkew")
