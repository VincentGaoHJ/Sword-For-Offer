# coding=utf-8
"""
@Time   : 2020/8/15  10:07 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 41. 数据流中的中位数
    https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/
"""

from heapq import *


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []  # 小顶堆，保存较大的一半
        self.B = []  # 大顶堆，保存较小的一半

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 通过判断两栈数量是否相等来控制每次新加入的数会导致哪个栈长度的增加
        if len(self.A) != len(self.B):
            heappush(self.A, num)  # 将数放入 A 栈中
            heappush(self.B, -heappop(self.A))  # 然后将 A 栈最小的拿出去并且取反放在 B 中，目的为了维护 B 为一个大顶堆
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self):
        """
        :rtype: float
        """
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0


def offer_41(order_lst, value_lst):
    """
    如何得到一个数据流中的中位数？
    如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
    如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
    例如，
    [2,3,4] 的中位数是 3
    [2,3] 的中位数是 (2 + 3) / 2 = 2.5
    设计一个支持以下两种操作的数据结构：
        void addNum (int num) - 从数据流中添加一个整数到数据结构中。
        double findMedian () - 返回目前所有元素的中位数。
    :param order_lst:
    :param value_lst:
    :return:
    """
    print(10 * "*")
    if len(order_lst) != len(value_lst):
        return False
    if order_lst[0] != 'MedianFinder':
        return False
    obj = MedianFinder()

    for (order, value) in zip(order_lst[1:], value_lst[1:]):
        if order == "addNum":
            obj.addNum(value[0])
            print('null')

        elif order == "findMedian":
            param_2 = obj.findMedian()
            print(param_2)


if __name__ == '__main__':
    # 剑指 Offer 41. 数据流中的中位数

    # 输出：[null,null,null,1.50000,null,2.00000]
    offer_41(order_lst=["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
             value_lst=[[], [1], [2], [], [3], []])

    # 输出：[null,null,2.00000,null,2.50000]
    offer_41(order_lst=["MedianFinder", "addNum", "findMedian", "addNum", "findMedian"],
             value_lst=[[], [2], [], [3], []])
