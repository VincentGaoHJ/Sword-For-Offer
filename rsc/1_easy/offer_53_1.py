# coding=utf-8
"""
@Time   : 2020/10/25  11:47 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 53 - I. 在排序数组中查找数字 I
    https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 搜索右边界
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j = mid - 1
        right = i

        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target:
            return 0

        # 搜索左边界 left
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j
        return right - left - 1


def offer_53_1(nums, target):
    """
    统计一个数字在排序数组中出现的次数。
    :param nums:
    :param target:
    :return:
    """
    solution = Solution()
    output = solution.search(nums, target)

    print(output)


# 本题要求统计数字 target 的出现次数
# 可转化为：使用二分法分别找到 左边界 left 和 右边界 right
# 易得数字 target 的数量为 right - left - 1。
if __name__ == '__main__':
    # 剑指 Offer 53 - I. 在排序数组中查找数字 I
    offer_53_1(nums=[5, 7, 7, 8, 8, 10], target=8)
    offer_53_1(nums=[5, 7, 7, 8, 8, 10], target=6)
