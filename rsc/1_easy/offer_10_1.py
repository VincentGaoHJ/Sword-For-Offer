# coding=utf-8
"""
@Time   : 2020/7/23  20:25 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 10-I. 斐波那契数列
    https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b  # 先计算 = 号的右边 b 的值，a+b 的值，算好了，然后再分别赋值给 a 和 b
        return a % 1000000007


def offer_10_1():
    """
    写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
        F(0) = 0,   F(1) = 1
        F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
    斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

    输入：n = 2
    输出：1

    提示：
    0 <= n <= 100
    :return:
    """

    n = 2

    solution = Solution()
    answer = solution.fib(n)

    print(answer)


if __name__ == '__main__':
    # 剑指 Offer 10-I. 斐波那契数列
    offer_10_1()
