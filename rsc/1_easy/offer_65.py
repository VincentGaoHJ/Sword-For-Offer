# coding=utf-8
"""
@Time   : 2020/10/30  12:47 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 65. 不用加减乘除做加法
    https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/
"""


class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


def offer_(a, b):
    """
    写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
    :param a:
    :param b:
    :return:
    """
    solution = Solution()
    output = solution.add(a, b)

    print(output)


# 正数与边界数 0xffffffff: 2**32-1, 即除去符号位，31 个 1
# 按位与 & 操作后仍得到这个数本身
# 负数与边界数按位与 & 操作后得到的是对应二进制数的真值（绝对值）
# (真值 - 1) 和 边界做 & 的反操作，即 ^, 可以得到负数的真值，加上 - 号，就是原来的负数.
# 如 num = -4
# -4 & (2**32-1) = 4294967292
# (4294967292 - 1) ^ (2**32-1) = 4 #
# 加上 - 号 即原来的 -4
if __name__ == '__main__':
    # 剑指 Offer 65. 不用加减乘除做加法
    offer_(a=1, b=1)
