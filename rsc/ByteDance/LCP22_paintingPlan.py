# coding=utf-8
"""
@Time   : 2020/12/1  16:28 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 黑白方格画
    https://leetcode-cn.com/problems/ccw6C7/
"""

import math


class Solution(object):
    def paintingPlan(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n * n == k:
            return 1
        plan_num = 0
        for i in range(0, n + 1):
            for j in range(0, n + 1):
                num = (i + j) * n - i * j
                if num == k:
                    comb_i = math.factorial(n) / (math.factorial(n - i) * math.factorial(i))
                    comb_j = math.factorial(n) / (math.factorial(n - j) * math.factorial(j))
                    plan_num += comb_i * comb_j
        return plan_num


def solution(n, k):
    """
    小扣注意到秋日市集上有一个创作黑白方格画的摊位。摊主给每个顾客提供一个固定在墙上的白色画板，画板不能转动。画板上有 n * n 的网格。绘画规则为，小扣可以选择任意多行以及任意多列的格子涂成黑色，所选行数、列数均可为 0。
    小扣希望最终的成品上需要有 k 个黑色格子，请返回小扣共有多少种涂色方案。
    注意：两个方案中任意一个相同位置的格子颜色不同，就视为不同的方案。
    :param n:
    :param k:
    :return:
    """
    solution = Solution()
    output = solution.paintingPlan(n, k)

    print(output)


if __name__ == '__main__':
    # 黑白方格画
    solution(n=2, k=2)
