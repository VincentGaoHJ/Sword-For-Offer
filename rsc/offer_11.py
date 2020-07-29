# coding=utf-8
"""
@Time   : 2020/7/29  10:10 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 11. 旋转数组的最小数字
    https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
"""


# class Solution:
#     def minArray(self, numsber: List[int]) -> int:
#         l, r = 0, len(numsber) - 1
#         while l<r:
#             m = (l+r)//2
#             if numsber[m]>numsber[r]:
#                 l = m+1
#             elif numsber[r]>numsber[m]:
#                 r = m
#             else:
#                 r -= 1
#         return numsber[l]


class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """

        left, right = 0, len(numbers) - 1

        while left < right:
            pivot = (right + left) // 2
            if numbers[pivot] > numbers[right]:
                left = pivot + 1
            elif numbers[pivot] < numbers[left]:
                right = pivot
            else:
                right -= 1

        return numbers[left]


def offer_11():
    """
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
    输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
    例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为 1。  

    输入：[3,4,5,1,2]
    输出：1

    :return:
    """
    numbers = [3, 4, 5, 1, 2]

    solution = Solution()
    output = solution.minArray(numbers)

    print(output)


# 还是二分查找的思路
# 初始化左和右
# 如果左小于右则循环
# 中间等于左和右的平均索引
# 如果中间和右边的值一样：移动左
# 如果中间大于右：左等于中间的下一个
# 如果右大于中间：右等于中间的下一个

if __name__ == '__main__':
    # 剑指 Offer 11. 旋转数组的最小数字
    offer_11()
