# coding=utf-8
"""
@Time   : 2020/10/26  11:38 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 57. 和为 s 的两个数字
    https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return nums[i], nums[j]
        return []


def offer_(nums, target):
    """
    输入一个递增排序的数组和一个数字 s，在数组中查找两个数，使得它们的和正好是 s。
    如果有多对数字的和等于 s，则输出任意一对即可。
    :param nums:
    :param target:
    :return:
    """
    solution = Solution()
    output = solution.twoSum(nums, target)

    print(output)


# 正确性证明：
# 记每个状态为 S(i, j)，即 S(i,j)=nums[i]+nums[j] 。假设 S(i,j)<target ，则执行 i=i+1 ，即状态切换至 S(i+1,j) 。
# 状态 S(i,j) 切换至 S(i+1,j) ，则会消去一行元素，相当于 消去了状态集合 {S(i,i+1),S(i,i+2),...,S(i,j−2),S(i,j−1),S(i,j) } 。
# （由于双指针都是向中间收缩，因此这些状态之后不可能再遇到）。
# 由于 nums 是排序数组，因此这些 消去的状态 都一定满足 S(i,j)<target ，即这些状态都 不是解 。
# 结论： 以上分析已证明 “每次指针 i 的移动操作，都不会导致解的丢失” ，即指针 i 的移动操作是 安全的 ；
# 同理，对于指针 j 可得出同样推论；因此，此双指针法是正确的。

if __name__ == '__main__':
    # 剑指 Offer 57. 和为 s 的两个数字
    offer_(nums=[2, 7, 11, 15], target=9)
    offer_(nums=[10, 26, 30, 31, 47, 60], target=40)
