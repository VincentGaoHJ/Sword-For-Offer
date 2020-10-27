# coding=utf-8
"""
@Time   : 2020/10/27  10:29 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 59 - I. 滑动窗口的最大值
    https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/
"""

import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        # deque: a double-ended queue
        deque = collections.deque()

        # 未形成窗口
        for i in range(k):
            # 删除 deque 内所有 <nums[j] 的元素，以保持 deque 递减
            while deque and deque[-1] < nums[i]:
                deque.pop()
            # 将 nums[j] 添加至 deque 尾部
            deque.append(nums[i])

        res = [deque[0]]

        # 形成窗口后
        for i in range(k, len(nums)):
            # 若 i > 0 且队首元素 deque[0] == 被删除元素 nums[i−1] ：则队首元素出队
            if deque[0] == nums[i - k]:
                deque.popleft()
            # 删除 deque 内所有 <nums[j] 的元素，以保持 deque 递减
            while deque and deque[-1] < nums[i]:
                deque.pop()
            # 将 nums[j] 添加至 deque 尾部
            deque.append(nums[i])
            # 将窗口最大值（即队首元素 deque[0]）添加至列表 res
            res.append(deque[0])
        return res


def offer_59_1(nums, k):
    """
    给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
    :param nums:
    :param k:
    :return:
    """
    solution = Solution()
    output = solution.maxSlidingWindow(nums, k)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 59 - I. 滑动窗口的最大值
    offer_59_1(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
