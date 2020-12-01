# coding=utf-8
"""
@Time   : 2020/12/1  12:02 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Next Permutation
    https://leetcode-cn.com/problems/next-permutation/
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        tmp_max = 0
        pivot_idx = -1
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] < tmp_max:
                pivot_idx = idx
                break
            tmp_max = max(nums[idx], tmp_max)
        if pivot_idx == -1:
            nums.reverse()
        else:
            for idx in range(len(nums) - 1, pivot_idx, -1):
                if nums[pivot_idx] < nums[idx]:
                    tmp = nums[idx]
                    nums[idx] = nums[pivot_idx]
                    nums[pivot_idx] = tmp
                    break
            left, right = pivot_idx + 1, len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1


def solution(nums):
    """
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such an arrangement is not possible, it must rearrange it as the lowest possible order
    (i.e., sorted in ascending order).
    The replacement must be in place and use only constant extra memory
    :param nums:
    :return:
    """
    solution = Solution()
    output = solution.nextPermutation(nums)

    print(output)


if __name__ == '__main__':
    # Next Permutation
    solution(nums=[1, 2, 3])
