# coding=utf-8
"""
@Time   : 2020/10/26  10:41 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 56 - I. 数组中数字出现的次数
    https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
"""


class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # ret 存放所有数字异或的结果
        # 可以知道 res = p ^ q,  其中 p, q 是我们想要知道的
        # 由于异或运算的性质是，数值不同时返回1，因此将 nums 按 res 数位最低的 1 分组
        # 比如 res = 1110，最低的1出现在第二位（第一位是0），
        # 因此可以按照 【第二个数位是 0 还是 1】 将 nums 分为两组，
        # 显然，p 和 q 一定落在不同的组。
        # 假设 p 落在组A，q 落在组B，
        # 则组A的特点是除了 p 出现一次之外，其他所有数字都出现了两次，组B同理也有这样的特点。
        ret, a, b = 0, 0, 0
        for num in nums:
            print(bin(ret))
            ret ^= num
        print(bin(ret))

        # 找到第一位不是0的
        h = 1
        # << bitwise shift operators
        # Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros).
        # This is the same as multiplying x by 2**y.
        while ret & h == 0:
            h <<= 1

        for num in nums:
            # 根据该位是否为0将其分为两组
            if h & num == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]


def offer_56_1(nums):
    """
    一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
    要求时间复杂度是 O (n)，空间复杂度是 O (1)。
    :param nums:
    :return:
    """
    solution = Solution()
    output = solution.singleNumbers(nums)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 56 - I. 数组中数字出现的次数
    offer_56_1(nums=[4, 1, 4, 6])
    offer_56_1(nums=[1, 2, 10, 4, 1, 4, 3, 3])
