# coding=utf-8
"""
@Time   : 2020/10/27  9:59 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 58 - II. 左旋转字符串
"""


class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:] + s[:n]


def offer_58_2(s, n):
    """
    字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
    请定义一个函数实现字符串左旋转操作的功能。
    比如，输入字符串 "abcdefg" 和数字 2，该函数将返回左旋转两位得到的结果 "cdefgab"。
    :param s:
    :param n:
    :return:
    """
    solution = Solution()
    output = solution.reverseLeftWords(s, n)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 58 - II. 左旋转字符串
    offer_58_2(s="abcdefg", n=2)
