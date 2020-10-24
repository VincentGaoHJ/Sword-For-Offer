# coding=utf-8
"""
@Time   : 2020/10/24  11:00 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 47. 礼物的最大价值
    https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
"""


class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


def offer_47(grid):
    """
    在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
    你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
    给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
    :param grid:
    :return:
    """
    solution = Solution()
    output = solution.maxValue(grid)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 47. 礼物的最大价值
    # 输出: 12
    # 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    offer_47(grid)

    grid = [[1, 2, 5],
            [3, 2, 1]]
    offer_47(grid)
