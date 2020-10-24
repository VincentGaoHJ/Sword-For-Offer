# coding=utf-8
"""
@Time   : 2020/10/23  22:05 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 44. 数字序列中某一位的数字
    https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit, start, count = 1, 1, 9
        # 确定所求数位的所在数字的位数
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9*start*digit
        # 确定所求数位所在的数字
        num = start + (n-1) // digit
        # 确定所求数位在 num 的哪一数位
        return int(str(num)[(n - 1) % digit])


def offer_44(n):
    """
    数字以 0123456789101112131415… 的格式序列化到一个字符序列中。
    在这个序列中，第 5 位（从下标 0 开始计数）是 5，第 13 位是 1，第 19 位是 4，等等。
    请写一个函数，求任意第 n 位对应的数字。
    :param n:
    :return:
    """
    solution = Solution()
    output = solution.findNthDigit(n)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 44. 数字序列中某一位的数字
    offer_44(n=3)
