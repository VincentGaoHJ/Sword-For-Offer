# coding=utf-8
"""
@Time   : 2020/10/22  10:22 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 31. 栈的压入、弹出序列
    https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
"""


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """

        stack, i = [], 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack


def offer_31(pushed, popped):
    """
    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
    假设压入栈的所有数字均不相等。
    例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，
    但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
    :param pushed:
    :param popped:
    :return:
    """
    solution = Solution()
    output = solution.validateStackSequences(pushed, popped)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 31. 栈的压入、弹出序列

    # 输出：true
    offer_31(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])

    # 输出：false
    # 解释：1 不能在 2 之前弹出。
    offer_31(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2])
