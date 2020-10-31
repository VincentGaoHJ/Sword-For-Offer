# coding=utf-8
"""
@Time   : 2020/10/30  12:57 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 66. 构建乘积数组
    https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
"""


class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]  # 下三角
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]  # 上三角
            b[i] *= tmp  # 下三角 * 上三角
        return b


def offer_66(a):
    """
    给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]
    其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]
    不能使用除法
    :param a:
    :return:
    """
    solution = Solution()
    output = solution.constructArr(a)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 66. 构建乘积数组
    offer_66([1, 2, 3, 4, 5])
