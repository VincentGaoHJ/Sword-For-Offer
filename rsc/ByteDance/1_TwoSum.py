# coding=utf-8
"""
@Time   : 2020/11/24  15:05 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for idx, value in enumerate(nums):
            hashmap[value] = idx
        for idx, value in enumerate(nums):
            idx2 = hashmap.get(target - value)
            if idx2 is not None and idx != idx2:
                return [idx, idx2]


def solution(nums, target):
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    :param nums:
    :param target:
    :return:
    """
    solution = Solution()
    output = solution.twoSum(nums, target)

    print(output)


# 解题思路，利用哈希表进行寻找
if __name__ == '__main__':
    solution(nums=[2, 7, 11, 15], target=9)
