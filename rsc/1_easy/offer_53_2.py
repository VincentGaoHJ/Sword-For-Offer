# coding=utf-8
"""
@Time   : 2020/10/26  10:12 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 53 - II. 0～n-1 中缺失的数字
    https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i


def offer_53_2(nums):
    """
    一个长度为 n-1 的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围 0～n-1 之内。
    在范围 0～n-1 内的 n 个数字中有且只有一个数字不在该数组中，请找出这个数字。
    :param nums:
    :return:
    """
    solution = Solution()
    output = solution.missingNumber(nums)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 53 - II. 0～n-1 中缺失的数字
    offer_53_2([0])
    offer_53_2([0, 1])
    offer_53_2([0, 1, 3])
    offer_53_2([0, 1, 2, 3, 4, 5, 6, 7, 9])
