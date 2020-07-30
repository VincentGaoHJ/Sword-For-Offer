# coding=utf-8
"""
@Time   : 2020/7/30  19:49 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 05. 替换空格
"""


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        return '%20'.join(s.split(' '))

    def replaceSpace_2(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.replace(' ', '%20')


def offer_05():
    """
    请实现一个函数，把字符串 s 中的每个空格替换成 "%20"。

    输入：s = "We are happy."
    输出："We%20are%20happy."
    限制：0 <= s 的长度 <= 10000

    :return:
    """

    s = "We are happy."

    solution = Solution()
    output = solution.replaceSpace(s)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 05. 替换空格
    offer_05()
