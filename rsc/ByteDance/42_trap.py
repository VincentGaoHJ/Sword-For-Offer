# coding=utf-8
"""
@Time   : 2020/11/27  15:13 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Trapping Rain Water
    https://leetcode-cn.com/problems/trapping-rain-water/
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right_max_lst, left_max_lst = [], []
        right_max, left_max = 0, 0
        for i in height:
            right_max = max(right_max, i)
            right_max_lst.append(right_max)
        for i in height[::-1]:
            left_max = max(left_max, i)
            left_max_lst.append(left_max)
        left_max_lst = left_max_lst[::-1]

        num = 0
        for right, value, left in zip(right_max_lst, height, left_max_lst):
            num += max(0, min(right, left) - value)
        return num


def solution(height):
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.
    :param height:
    :return:
    """
    solution = Solution()
    output = solution.trap(height)

    print(output)


if __name__ == '__main__':
    # Trapping Rain Water

    # Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # Output: 6
    # Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
    # In this case, 6 units of rain water (blue section) are being trapped.
    solution(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
