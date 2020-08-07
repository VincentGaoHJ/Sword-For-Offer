# coding=utf-8
"""
@Time   : 2020/8/7  11:43 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 16. 数值的整数次方
    https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            return self.myPow(x * x, int(n / 2)) if not n & 1 else x * self.myPow(x, n - 1)


def offer_16(x, n):
    """
    实现函数 double Power (double base, int exponent)，求 base 的 exponent 次方。
    不得使用库函数，同时不需要考虑大数问题。
    说明: -100.0 < x < 100.0; n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
    :return:
    """
    solution = Solution()
    output = solution.myPow(x, n)
    print(output)


if __name__ == '__main__':
    # 剑指 Offer 16. 数值的整数次方
    offer_16(2.00000, 10)  # 1024.00000
    offer_16(2.10000, 3)  # 9.26100
    offer_16(2.00000, -2)  # 0.25000
