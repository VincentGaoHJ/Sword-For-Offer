# coding=utf-8
"""
@Time   : 2020/8/2  9:46 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 14- II. 剪绳子 II
    https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/
"""
import math


class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 3:
            return int(n - 1 % (1e9+7))
        a, b = n // 3, n % 3

        if b == 0:
            return (3 ** a) % int(1e9+7)
        elif b == 1:
            return (3 ** (a - 1) * 4) % int(1e9+7)
        else:
            return (3 ** a * 2) % int(1e9+7)


def offer_14_2():
    """
    给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n 都是整数，n>1 并且 m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1]。
    请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？
    例如，当绳子的长度是 8 时，我们把它剪成长度分别为 2、3、3 的三段，此时得到的最大乘积是 18。
    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
    输入: 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1
    提示：2 <= n <= 1000
    :return:
    """

    n = 2

    solution = Solution()
    output = solution.cuttingRope(n)

    print(n)


if __name__ == '__main__':
    # 剑指 Offer 14- II. 剪绳子 II
    offer_14_2()
