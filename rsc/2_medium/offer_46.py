# coding=utf-8
"""
@Time   : 2020/10/24  10:40 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 46. 把数字翻译成字符串
    https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
"""


class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 1
        elif num % 100 > 25 or 0 <= num % 100 <= 9:
            return self.translateNum(num // 10)
        elif 10 <= num % 100 <= 25:
            return self.translateNum(num // 100) + self.translateNum(num // 10)


def offer_46(num):
    """
    给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
    一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
    :param num:
    :return:
    """
    solution = Solution()
    output = solution.translateNum(num)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 46. 把数字翻译成字符串
    offer_46(12258)
