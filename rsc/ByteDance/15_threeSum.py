# coding=utf-8
"""
@Time   : 2020/11/28  11:22 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 3Sum
    https://leetcode-cn.com/problems/3sum/
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        ans = []

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = n - 1
            target = -nums[first]
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans


def solution(nums):
    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.
    Notice that the solution set must not contain duplicate triplets.

    :param nums:
    :return:
    """
    solution = Solution()
    output = solution.threeSum(nums)

    print(output)


# 思路：排序＋双指针
if __name__ == '__main__':
    # 3Sum

    solution(nums=[-1, 0, 1, 2, -1, -4])
    solution(nums=[0, 0, 0])
