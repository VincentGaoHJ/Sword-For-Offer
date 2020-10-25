# coding=utf-8
"""
@Time   : 2020/10/25  10:14 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 51. 数组中的逆序对
    https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
"""


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)

    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2

        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)

        i, j, pos = l, mid + 1, l

        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
            else:
                tmp[pos] = nums[j]
                j += 1
                inv_count += mid + 1 - i
            pos += 1

        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            pos += 1

        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1

        nums[l:r + 1] = tmp[l:r + 1]
        return inv_count


def offer_51(nums):
    """
    在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
    输入一个数组，求出这个数组中的逆序对的总数。
    :param nums:
    :return:
    """
    solution = Solution()
    output = solution.reversePairs(nums)
    print(output)


if __name__ == '__main__':
    # 剑指 Offer 51. 数组中的逆序对
    offer_51([7, 5, 6, 4])
    offer_51([1, 3, 2, 3, 1])
