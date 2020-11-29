# coding=utf-8
"""
@Time   : 2020/11/29  11:23 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Search in Rotated Sorted Array
    https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        max_idx = len(nums) - 1
        if nums[0] <= nums[-1]:
            pivot = 0
            while target > nums[pivot]:
                if pivot == max_idx:
                    break
                pivot += 1
            if target == nums[pivot]:
                return pivot
            else:
                return -1
        if nums[-1] < target:
            pivot = 0
            while target > nums[pivot] > nums[-1]:
                pivot += 1
            if target == nums[pivot]:
                return pivot
            else:
                return -1
        else:
            pivot = len(nums) - 1
            while target < nums[pivot] <= nums[0]:
                if pivot == 0:
                    break
                pivot -= 1
            if target == nums[pivot]:
                return pivot
            else:
                return -1


def solution(nums, target):
    """
    You are given an integer array nums sorted in ascending order, and an integer target.
    Suppose that nums is rotated at some pivot unknown to you beforehand
    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
    If target is found in the array return its index, otherwise, return -1.
    :param nums:
    :param target:
    :return:
    """
    solution = Solution()
    output = solution.search(nums, target)

    print(output)


if __name__ == '__main__':
    # Search in Rotated Sorted Array
    solution(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
    solution(nums=[1, 3], target=1)
    solution(nums=[1], target=2)
    solution(nums=[1, 3], target=3)
    solution(nums=[3, 1], target=1)
