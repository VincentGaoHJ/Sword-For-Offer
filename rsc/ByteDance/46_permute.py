# coding=utf-8
"""
@Time   : 2020/12/1  11:12 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Permutations
    https://leetcode-cn.com/problems/permutations/
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        permu_lst = []
        for idx in range(len(nums)):
            tmp_lst = nums[:idx] + nums[idx + 1:]
            tmp_permute = self.permute(tmp_lst)
            tmp_permute = [[nums[idx]] + i for i in tmp_permute]
            permu_lst += tmp_permute
        return permu_lst


def solution(nums):
    """
    Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.
    :param nums:
    :return:
    """
    solution = Solution()
    output = solution.permute(nums)

    print(output)


if __name__ == '__main__':
    # Permutations
    solution(nums=[1, 2, 3])
