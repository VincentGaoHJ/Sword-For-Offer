# coding=utf-8
"""
@Time   : 2020/10/29  9:42 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 60. n 个骰子的点数
    https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/
"""


class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        if n == 0:
            return []

        # 初始化 1 - 6 是 1次，7 - n 是 0 次。
        # 编号从1开始，这样方便写代码。  为了从1开始，我们只需要在数组前面随便push一个元素即可，比如本例的0
        cnts = [0] + [1] * 6 + [0] * (6 * n - 6)
        # 模拟投掷 n - 1 次
        for _ in range(n - 1):
            # 从后向前更新
            for i in range(6 * n, 0, -1):
                cnts[i] = sum(cnts[max(i - 6, 0): i])

        return list(filter(lambda a: a != 0, list(map(lambda a: a / (6 ** n), cnts))))


def offer_60(n):
    """
    把 n 个骰子扔在地上，所有骰子朝上一面的点数之和为 s。
    输入 n，打印出 s 的所有可能的值出现的概率。
    你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
    :param n:
    :return:
    """
    solution = Solution()
    output = solution.twoSum(n)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 60. n 个骰子的点数
    offer_60(1)
    offer_60(2)
