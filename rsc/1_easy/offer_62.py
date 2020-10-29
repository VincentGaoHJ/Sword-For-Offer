# coding=utf-8
"""
@Time   : 2020/10/29  10:38 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 62. 圆圈中最后剩下的数字
    https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
"""


def f(n, m):
    if n == 0:
        return 0
    x = f(n - 1, m)
    return (m + x) % n


class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        return f(n, m)


def offer_62(n, m):
    """
    0,1,,n-1 这 n 个数字排成一个圆圈，从数字 0 开始，每次从这个圆圈里删除第 m 个数字。
    求出这个圆圈里剩下的最后一个数字。
    例如，0、1、2、3、4 这 5 个数字组成一个圆圈，从数字 0 开始每次删除第 3 个数字，
    则删除的前 4 个数字依次是 2、0、4、1，因此最后剩下的数字是 3。
    :param n:
    :param m:
    :return:
    """
    solution = Solution()
    output = solution.lastRemaining(n, m)

    print(output)


# 因此我们可以推出递推公式f(8,3)=[f(7,3)+3]%8
# 进行推广泛化，即f(n,m)=[f(n−1,m)+m]%n
if __name__ == '__main__':
    # 剑指 Offer 62. 圆圈中最后剩下的数字
    offer_62(n=5, m=3)
    offer_62(n=10, m=17)
