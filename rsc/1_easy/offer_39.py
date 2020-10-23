# coding=utf-8
"""
@Time   : 2020/10/22  11:28 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 39. 数组中出现次数超过一半的数字
    https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[int(len(nums) / 2)]


def offer_39(nums):
    """
    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    你可以假设数组是非空的，并且给定的数组总是存在多数元素。
    :param nums:
    :return:
    """
    # 答案一定是排序后的数组的中间元素
    solution = Solution()
    output = solution.majorityElement(nums)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 39. 数组中出现次数超过一半的数字
    offer_39(nums=[1, 2, 3, 2, 2, 2, 5, 4, 2])
