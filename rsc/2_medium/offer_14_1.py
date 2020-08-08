# coding=utf-8
"""
@Time   : 2020/8/2  9:12 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 14- I. 剪绳子
    https://leetcode-cn.com/problems/jian-sheng-zi-lcof/
"""

import math


class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Python 中常见有三种幂计算函数：
        # * 和 pow() 的时间复杂度均为 O(loga) ；
        # 而 math.pow() 始终调用 C 库的 pow() 函数，其执行浮点取幂，时间复杂度为 O(1)O(1) 。

        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3

        if b == 0:
            return int(math.pow(3, a))
        elif b == 1:
            return int(math.pow(3, a - 1) * 4)
        else:
            return int(math.pow(3, a) * 2)


def offer_14_1():
    """
    给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n 都是整数，n>1 并且 m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
    请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
    例如，当绳子的长度是 8 时，我们把它剪成长度分别为 2、3、3 的三段，此时得到的最大乘积是 18。
    输入: 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1
    提示：2 <= n <= 58
    :return:
    """

    n = 2

    solution = Solution()
    output = solution.cuttingRope(n)

    print(output)


# 最优：3。把绳子尽可能切为多个长度为 3 的片段，留下的最后一段绳子的长度可能为 0, 1, 2 三种情况。
# 次优：2。若最后一段绳子长度为 2 ；则保留，不再拆为 1 + 1。
# 最差：1。若最后一段绳子长度为 1 ；则应把一份 3 + 1 替换为 2 + 2，因为 2 × 2 > 3 × 1。

# 当 n ≤ 3 时，按照规则应不切分，但由于题目要求必须剪成 m > 1 段，因此必须剪出一段长度为 1 的绳子，即返回 n - 1。
# 当 n > 3 时，求 n 除以 3 的 整数部分 a 和 余数部分 b，即 n = 3a + b，并分为以下三种情况：
# 当 b = 0 时，直接返回 3^a
# 当 b = 1 时，要将一个 1 + 3 转换为 2 + 2，因此返回 3^{a-1} × 4
# 当 b = 2 时，返回 3^a × 2
if __name__ == '__main__':
    # 剑指 Offer 14- I. 剪绳子
    offer_14_1()
