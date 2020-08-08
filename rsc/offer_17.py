# coding=utf-8
"""
@Time   : 2020/8/8  11:33 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 17. 打印从 1 到最大的 n 位数
    https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
"""


class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return list(range(1, 10 ** n))


def offer_17(n):
    """
    输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
    输入: n = 1
    输出: [1,2,3,4,5,6,7,8,9]
    说明：用返回一个整数列表来代替打印; n 为正整数
    :param n:
    :return:
    """
    solution = Solution()
    output = solution.printNumbers(n)

    print(output)


# 利用 Python 的语言特性，可以简化代码：
# 先使用 range() 方法生成可迭代对象，再使用 list() 方法转化为列表并返回即可
if __name__ == '__main__':
    # 剑指 Offer 17. 打印从 1 到最大的 n 位数
    offer_17(1)
    offer_17(2)
