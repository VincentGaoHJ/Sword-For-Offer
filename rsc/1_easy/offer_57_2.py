# coding=utf-8
"""
@Time   : 2020/10/27  9:32 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 57 - II. 和为 s 的连续正数序列
    https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
"""


class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """

        i, j, res = 1, 2, []
        while j <= target // 2 + 1:
            cur_sum = sum(list(range(i, j + 1)))
            if cur_sum < target:
                j += 1
            elif cur_sum > target:
                i += 1
            else:
                res.append(list(range(i, j + 1)))
                j += 1
        return res


def offer_57_2(target):
    """
    输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）
    序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
    :param target:
    :return:
    """
    solution = Solution()
    output = solution.findContinuousSequence(target)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 57 - II. 和为 s 的连续正数序列

    # 输出：[[2,3,4],[4,5]]
    offer_57_2(target=9)
