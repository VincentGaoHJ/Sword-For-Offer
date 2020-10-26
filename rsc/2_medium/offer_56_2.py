# coding=utf-8
"""
@Time   : 2020/10/26  11:36 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 56 - II. 数组中数字出现的次数 II
    https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i, j in dic.items():
            if j == 1:
                return i


def offer_56_2(nums):
    """
    在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。
    请找出那个只出现一次的数字。
    :param nums:
    :return:
    """
    solution = Solution()
    output = solution.singleNumber(nums)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 56 - II. 数组中数字出现的次数 II
    offer_56_2(nums=[3, 4, 3, 3])
