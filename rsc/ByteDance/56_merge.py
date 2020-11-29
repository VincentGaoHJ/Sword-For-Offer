# coding=utf-8
"""
@Time   : 2020/11/29  16:11 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Merge Intervals
    https://leetcode-cn.com/problems/merge-intervals/
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        merged_lst = []
        for interval in intervals:
            if not merged_lst or merged_lst[-1][-1] < interval[0]:
                merged_lst.append(interval)
            else:
                merged_lst[-1][-1] = max(merged_lst[-1][-1], interval[1])
        return merged_lst


def solution(intervals):
    """
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
    and return an array of the non-overlapping intervals that cover all the intervals in the input.
    :param intervals:
    :return:
    """
    solution = Solution()
    output = solution.merge(intervals)

    print(output)


if __name__ == '__main__':
    # Merge Intervals
    solution(intervals=[[1, 3], [8, 10], [2, 6], [15, 18]])
