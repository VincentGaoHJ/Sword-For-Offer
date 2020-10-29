# coding=utf-8
"""
@Time   : 2020/10/29  10:15 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 61. 扑克牌中的顺子
    https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
"""


class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        repeat = set()
        max_num, min_num = 0, 14
        for num in nums:
            if num == 0:  # 跳过大小王
                continue
            max_num = max(max_num, num)  # 最大牌
            min_num = min(min_num, num)  # 最小牌
            if num in repeat:  # 若有重复，提前返回 false
                return False
            repeat.add(num)  # 添加牌至 Set

        return max_num - min_num < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


def offer_61(nums):
    """
    从扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这 5 张牌是不是连续的。
    2～10 为数字本身，A 为 1，J 为 11，Q 为 12，K 为 13，而大、小王为 0 ，可以看成任意数字。
    A 不能视为 14。
    :param nums:
    :return:
    """
    solution = Solution()
    output = solution.isStraight(nums)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 61. 扑克牌中的顺子
    offer_61([1, 2, 3, 4, 5])
