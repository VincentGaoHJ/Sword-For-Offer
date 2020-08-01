# coding=utf-8
"""
@Time   : 2020/8/1  14:33 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 13. 机器人的运动范围
    https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
"""

import collections


def sum_digits(num_lst):
    digit_sum = 0
    for num in num_lst:
        while num != 0:
            digit_sum += num % 10
            num //= 10
    return digit_sum


def depth_first_search(x, y, x_max, y_max, sum_max, visited):
    if x == x_max or y == y_max or sum_digits([x, y]) > sum_max or (x, y) in visited:
        return
    visited.add((x, y))
    depth_first_search(x + 1, y, x_max, y_max, sum_max, visited)
    depth_first_search(x, y + 1, x_max, y_max, sum_max, visited)
    return len(visited)


class Solution(object):
    def movingCount_BFS(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        visited = set()
        queue = collections.deque()
        queue.append((0, 0))

        while queue:
            x, y = queue.popleft()
            if (x, y) not in visited and sum_digits([x, y]) <= k:
                visited.add((x, y))
                if x + 1 < m:
                    queue.append((x + 1, y))
                if y + 1 < n:
                    queue.append((x, y + 1))
        return len(visited)

    def movingCount_DFS(self, m, n, k):
        visited = set()
        return depth_first_search(0, 0, m, n, k, visited)


def offer_13():
    """
    地上有一个 m 行 n 列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
    一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
    也不能进入行坐标和列坐标的数位之和大于 k 的格子。
    例如，当 k 为 18 时，机器人能够进入方格 [35, 37] ，因为 3+5+3+7=18。
    但它不能进入方格 [35, 38]，因为 3+5+3+8=19。
    请问该机器人能够到达多少个格子？

    输入：m = 2, n = 3, k = 1
    输出：3
    提示：1 <= n,m <= 100; 0 <= k <= 20

    :return:
    """
    m, n, k = 2, 3, 1

    solution = Solution()

    output = solution.movingCount_BFS(m, n, k)
    print(output)

    output = solution.movingCount_DFS(m, n, k)
    print(output)


# 典型的深度搜索和广度搜索问题
# 深度优先：用递归的思路解决
# 广度优先：用队列存储，while 中 pop 和 append
# 需要用到队列或者栈 collections.deque([])
if __name__ == '__main__':
    # 剑指 Offer 13. 机器人的运动范围
    offer_13()
