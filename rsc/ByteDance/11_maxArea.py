# coding=utf-8
"""
@Time   : 2020/11/29  10:57 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Container With Most Water
    https://leetcode-cn.com/problems/container-with-most-water/
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head, tail = 0, len(height) - 1
        max_area = 0
        while head != tail:
            cur_area = (tail - head) * min(height[head], height[tail])
            max_area = max(max_area, cur_area)
            if height[head] < height[tail]:
                head += 1
            else:
                tail -= 1
        return max_area


def solution(height):
    """
    Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
    Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
    Notice that you may not slant the container.
    :param height:
    :return:
    """
    solution = Solution()
    output = solution.maxArea(height)

    print(output)


# 双指针问题
if __name__ == '__main__':
    # Container With Most Water
    solution(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
