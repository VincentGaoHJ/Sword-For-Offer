# coding=utf-8
"""
@Time   : 2020/8/13  9:52 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 40. 最小的 k 个数
    https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
"""

import heapq

class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        return heapq.nsmallest(k, arr)


def offer_40(arr, k):
    """
    输入整数数组 arr ，找出其中最小的 k 个数。
    例如，输入 4、5、1、6、2、7、3、8 这 8 个数字，则最小的 4 个数字是 1、2、3、4。
    :param arr:
    :param k:
    :return:
    """
    solution = Solution()
    topK = solution.getLeastNumbers(arr, k)

    print(topK)


if __name__ == '__main__':
    # 剑指 Offer 40. 最小的 k 个数
    offer_40(arr=[3, 2, 1], k=2)  # 输出：[1,2] 或者 [2,1]
    offer_40(arr=[0, 1, 2, 1], k=1)  # 输出：[0]
