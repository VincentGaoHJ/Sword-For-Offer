# coding=utf-8
"""
@Time   : 2020/7/24  23:41 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 10- II. 青蛙跳台阶问题
    https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
"""


class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """

        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b  # 先计算 = 号的右边 b 的值，a+b 的值，算好了，然后再分别赋值给 a 和 b
        return a % 1000000007


def offer_10_2():
    """
    一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

    输入：n = 2
    输出：2
    提示：0 <= n <= 100

    :return:
    """


# 解题思路，应该上来就能想到应该是个递归算法，因为首先就是最后的状态被倒数第二种状态决定
# 接下来就应该正着想，能否总第一个状态或者前几个状态推断后面的状态，这样就不需要递归了，节省了空间和时间
# 总的来讲：
# 设跳上 n 级台阶有 f(n) 种跳法。在所有跳法中，青蛙的最后一步只有两种情况： 跳上 1 级或 2 级台阶。
# 当为 1 级台阶： 剩 n-1 个台阶，此情况共有 f(n−1) 种跳法；
# 当为 2 级台阶： 剩 n-2 个台阶，此情况共有 f(n−2) 种跳法。
# 所以：
# f(n+1) = f(n) + f(n−1)

if __name__ == '__main__':
    # 剑指 Offer 10- II. 青蛙跳台阶问题
    offer_10_2()
