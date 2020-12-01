# coding=utf-8
"""
@Time   : 2020/12/1  16:05 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 秋叶收藏集
    https://leetcode-cn.com/problems/UlBDOe/
"""


class Solution(object):
    def minimumOperations(self, leaves):
        """
        :type leaves: str
        :rtype: int
        """
        dp_r, dp_ry, dp_ryr = [float('inf')] * len(leaves), [float('inf')] * len(leaves), [float('inf')] * len(leaves)
        for idx, leave in enumerate(leaves):
            if idx == 0:
                if leave == 'r':
                    dp_r[idx] = 0
                else:
                    dp_r[idx] = 1
                continue
            if leave == 'r':
                dp_r[idx] = dp_r[idx - 1]
                dp_ry[idx] = min(dp_r[idx - 1], dp_ry[idx - 1]) + 1
                dp_ryr[idx] = min(dp_ry[idx - 1], dp_ryr[idx - 1])
            else:
                dp_r[idx] = dp_r[idx - 1] + 1
                dp_ry[idx] = min(dp_r[idx - 1], dp_ry[idx - 1])
                dp_ryr[idx] = min(dp_ry[idx - 1], dp_ryr[idx - 1]) + 1
        return dp_ryr[-1]


def solution(leaves):
    """
    小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves，
    字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
    出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，
    但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。
    请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。
    :param leaves:
    :return:
    """
    solution = Solution()
    output = solution.minimumOperations(leaves)

    print(output)


if __name__ == '__main__':
    # 秋叶收藏集
    solution(leaves="rrryyyrryyyrr")
