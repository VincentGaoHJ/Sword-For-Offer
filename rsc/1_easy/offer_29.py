# coding=utf-8
"""
@Time   : 2020/8/7  10:09 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 29. 顺时针打印矩阵
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral_lst = []
        while matrix:
            spiral_lst += matrix.pop(0)
            matrix = self.anticlockwise_rotation(matrix)

        return spiral_lst

    def anticlockwise_rotation(self, matrix):
        return list(zip(*matrix))[::-1]


def offer_29(matrix):
    """
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
    限制：
        0 <= matrix.length <= 100
        0 <= matrix[i].length <= 100
    :param matrix:
    :return:
    """

    solution = Solution()
    output = solution.spiralOrder(matrix)
    print(output)


# 顺时针打印等于打印一行之后逆时针旋转矩阵
# 逆时针旋转矩阵等于矩阵转置之后再上下翻转
# 矩阵转置等于将矩阵前面加星号将列表解开成两个独立的参数
# 再用 zip 纵向合成一个变量，同时用 list() 变换会一个矩阵
# 上下翻转用 [::-1]

if __name__ == '__main__':
    # 剑指 Offer 29. 顺时针打印矩阵
    offer_29([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Output: [1,2,3,6,9,8,7,4,5]
    offer_29([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
