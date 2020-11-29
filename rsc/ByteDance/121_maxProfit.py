# coding=utf-8
"""
@Time   : 2020/11/29  12:03 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Best Time to Buy and Sell Stock
    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


def solution(prices):
    """
    Say you have an array for which the ith element is the price of a given stock on day i.
    If you were only permitted to complete at most one transaction
    (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
    Note that you cannot sell a stock before you buy one.
    :param prices:
    :return:
    """
    solution = Solution()
    output = solution.maxProfit(prices)

    print(output)


if __name__ == '__main__':
    # Best Time to Buy and Sell Stock
    solution([7, 1, 5, 3, 6, 4])
