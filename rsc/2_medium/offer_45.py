# coding=utf-8
"""
@Time   : 2020/10/23  22:20 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 45. 把数组排成最小的数
    https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
"""


class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def partition(array, low, high):
            i = (low - 1)
            pivot = array[high]
            for j in range(low, high):
                if array[j] + pivot <= pivot + array[j]:
                    i = i + 1
                    array[i], array[j] = array[j], array[i]
            array[i + 1], array[high] = array[high], array[i + 1]
            return i + 1

        def quick_sort(array, low, high):
            if low < high:
                idx = partition(array, low, high)
                quick_sort(array, low, idx - 1)
                quick_sort(array, idx + 1, high)

        array = [str(num) for num in nums]

        low, high = 0, len(array) - 1

        quick_sort(array, low, high)

        return ''.join(array)


def offer_45(nums):
    """
    输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
    :param nums:
    :return:
    """
    solution = Solution()
    output = solution.minNumber(nums)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 45. 把数组排成最小的数
    offer_45([3, 30, 34, 5, 9])
