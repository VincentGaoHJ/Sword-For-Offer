# coding=utf-8
"""
@Time   : 2020/10/29  10:56 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 63. 股票的最大利润
    https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit


def offer_63(prices):
    """
    假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
    :param prices:
    :return:
    """
    solution = Solution()
    output = solution.maxProfit(prices)

    print(output)


# 状态定义： 设动态规划列表 dp ，dp[i] 代表以 prices[i] 为结尾的子数组的最大利润（以下简称为 前 i 日的最大利润 ）。
# 转移方程： 由于题目限定 “买卖该股票一次” ，因此前 i 日最大利润 dp[i] 等于前 i-1 日最大利润 dp[i−1] 和第 i 日卖出的最大利润中的最大值。
if __name__ == '__main__':
    # 剑指 Offer 63. 股票的最大利润
    offer_63([7, 1, 5, 3, 6, 4])
