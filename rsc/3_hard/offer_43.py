# coding=utf-8
"""
@Time   : 2020/10/22  10:59 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 43. 1～n 整数中 1 出现的次数
    https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/pythondi-gui-by-rainiee-pan/
"""


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        num_s = str(n)
        high = int(num_s[0])
        power = 10 ** (len(num_s) - 1)
        last = n - high * power
        if high == 1:
            # 假设 n = 1234
            # countDigitOne(power-1): 0 - 999 中 1 出现的个数 （1234 -> 1000 -> 999）
            # countDigitOne(last): 去除最高位之后低位中 1 出现的个数 (1234 -> 1000 -> 234)
            # last+1: 每一个低位都对应了一个高位 1
            return self.countDigitOne(power - 1) + self.countDigitOne(last) + last + 1
        else:
            # 假设 n = 2234
            # high * self.countDigitOne(power - 1): 代表 999 以内和 1999 以内低位出现的 1
            # power: 1000 - 1999 的高位 1 数量
            # self.countDigitOne(last): 同上
            return power + high * self.countDigitOne(power - 1) + self.countDigitOne(last)


def offer_(n):
    """
    输入一个整数 n ，求 1～n 这 n 个整数的十进制表示中 1 出现的次数。
    例如，输入 12，1～12 这些整数中包含 1 的数字有 1、10、11 和 12，1 一共出现了 5 次。
    :param n:
    :return:
    """
    solution = Solution()
    output = solution.countDigitOne(n)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 43. 1～n 整数中 1 出现的次数
    offer_(n=12)
