# coding=utf-8
"""
@Time   : 2020/7/23  21:03 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 03. 数组中重复的数字
    https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
"""


class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_set = set()
        for index, num in enumerate(nums):
            temp_set.add(num)
            if not index == len(temp_set)-1:
                return num


def offer_03():
    """
    在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数
    组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
    请找出数组中任意一个重复的数字。

    输入：[2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3
    限制：2 <= n <= 100000

    :return:
    """

    nums = [2, 3, 1, 0, 2, 5, 3]

    solution = Solution()
    repeatNumber = solution.findRepeatNumber(nums)

    print(repeatNumber)


if __name__ == '__main__':
    # 剑指 Offer 03. 数组中重复的数字
    offer_03()
