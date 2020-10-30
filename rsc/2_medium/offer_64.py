# coding=utf-8
"""
@Time   : 2020/10/30  12:37 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 64. 求 1+2+…+n
    https://leetcode-cn.com/problems/qiu-12n-lcof/
"""


class Solution(object):
    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        n > 1 and self.sumNums(n - 1)  # 逻辑短路终值递归
        self.res += n
        return self.res


def offer_64(n):
    """
    求 1+2+...+n
    要求不能使用乘除法、for、while、if、else、switch、case 等关键字及条件判断语句（A?B:C）
    :param n:
    :return:
    """
    solution = Solution()
    output = solution.sumNums(n)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 64. 求 1+2+…+n
    offer_64(n=3)
