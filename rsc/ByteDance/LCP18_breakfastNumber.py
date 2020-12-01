# coding=utf-8
"""
@Time   : 2020/12/1  12:25 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 早餐组合
    https://leetcode-cn.com/problems/2vYnGI/
"""


class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        """
        :type staple: List[int]
        :type drinks: List[int]
        :type x: int
        :rtype: int
        """
        sum = 0
        drinks.sort()
        staple.sort()
        tail_idx = len(drinks) - 1
        for head_idx in range(len(staple)):
            while staple[head_idx] + drinks[tail_idx] > x and tail_idx >= 0:
                tail_idx -= 1
            sum += tail_idx + 1
        return int(sum % (1e9 + 7))


def solution(staple, drinks, x):
    """
    小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，一维整型数组 drinks 中记录了每种饮料的价格。
    小扣的计划选择一份主食和一款饮料，且花费不超过 x 元。请返回小扣共有多少种购买方案。
    注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
    :param staple:
    :param drinks:
    :param x:
    :return:
    """
    solution = Solution()
    output = solution.breakfastNumber(staple, drinks, x)

    print(output)


if __name__ == '__main__':
    # 早餐组合
    solution(staple=[10, 20, 5], drinks=[5, 5, 2], x=15)
