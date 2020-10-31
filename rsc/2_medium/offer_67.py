# coding=utf-8
"""
@Time   : 2020/10/31  10:17 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 67. 把字符串转换成整数
"""


class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 删除首尾空格
        str = str.strip()
        # 字符串为空则直接返回
        if not str:
            return 0
        res, i, sign = 0, 1, 1
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        # 保存负号
        if str[0] == '-':
            sign = -1
        # 若无符号位，则需从 i = 0 开始数字拼接
        elif str[0] != '+':
            i = 0

        for c in str[i:]:
            # 遇到非数字的字符则跳出
            if not '0' <= c <= '9':
                break
            # 数字越界处理
            if res > bndry or res == bndry and c > '7':
                return int_max if sign == 1 else int_min
            # 数字拼接
            # ord() function returns an integer representing the Unicode character.
            res = 10 * res + ord(c) - ord('0')
        return sign * res


def offer_67(str):
    """
    写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。
    首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
    当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
    假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
    该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
    注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
    在任何情况下，若函数不能进行有效的转换时，请返回 0。
    :param str:
    :return:
    """
    solution = Solution()
    output = solution.strToInt(str)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 67. 把字符串转换成整数
    offer_67("42")
