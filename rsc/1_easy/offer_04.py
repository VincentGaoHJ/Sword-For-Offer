# coding=utf-8
"""
@Time   : 2020/7/23  21:28 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 04. 二维数组中的查找
    https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
"""


class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        elif not matrix[0]:
            return False
        x_max, y_max = len(matrix), len(matrix[0])
        x, y = 0, y_max - 1
        right_upper = matrix[x][y]
        if right_upper == target:
            return True
        elif right_upper > target:
            matrix_b = [row[:-1] for row in matrix]
        elif right_upper < target:
            matrix_b = matrix[1:]
        return self.findNumberIn2DArray(matrix_b, target)


def offer_04():
    """
    在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

    现有矩阵 matrix 如下：
    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    给定 target = 5，返回 true。
    给定 target = 20，返回 false。

    限制：
        0 <= n <= 1000
        0 <= m <= 1000

    :return:
    """

    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]

    target = 20

    solution = Solution()
    answer = solution.findNumberIn2DArray(matrix, target)

    print(answer)


if __name__ == '__main__':
    # 剑指 Offer 04. 二维数组中的查找
    offer_04()
