# coding=utf-8
"""
@Time   : 2020/12/3  19:09 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 
"""


class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """


def solution(n, k):
    """
    给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。
    注意：1 ≤ k ≤ n ≤ 109。
    输入: n: 13   k: 2
    输出: 10
    解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
    :param n:
    :param k:
    :return:
    """
    solution = Solution()
    output = solution.findKthNumber(n, k)

    print(output)


if __name__ == '__main__':
    solution()
