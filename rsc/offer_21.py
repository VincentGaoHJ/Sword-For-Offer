# coding=utf-8
"""
@Time   : 2020/8/6  20:31 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
    https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
"""


class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd_idx = 0
        for idx, num in enumerate(nums):
            if num % 2 == 1:
                nums[idx], nums[odd_idx] = nums[odd_idx], nums[idx]
                odd_idx += 1
        return nums


def offer_21(nums):
    """
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
    输入：nums = [1,2,3,4]
    输出：[1,3,2,4]
    注：[3,1,2,4] 也是正确的答案之一。
    提示：
        1 <= nums.length <= 50000
        1 <= nums[i] <= 10000
    :param nums: [list]
    :return:
    """
    solution = Solution()
    output = solution.exchange(nums)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
    offer_21([1, 2, 3, 4])
