# coding=utf-8
"""
@Time   : 2020/11/27  16:06 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Maximum Subarray
    https://leetcode-cn.com/problems/maximum-subarray/
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_sum = 0
        tmp_sum = 0
        if max(nums) <= 0:
            return max(nums)
        for i in nums:
            tmp_sum += i
            tmp_sum = max(tmp_sum, 0)
            largest_sum = max(largest_sum, tmp_sum)
        return largest_sum


def solution(nums):
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.
    Follow up: If you have figured out the O(n) solution,
    try coding another solution using the divide and conquer approach, which is more subtle.
    :param nums:
    :return:
    """
    solution = Solution()
    output = solution.maxSubArray(nums)

    print(output)


if __name__ == '__main__':
    # Maximum Subarray
    solution(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
