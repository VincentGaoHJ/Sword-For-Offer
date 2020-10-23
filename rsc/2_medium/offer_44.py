# coding=utf-8
"""
@Time   : 2020/10/23  22:05 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit, start, count = 1, 1, 9
        # 确定所求数位的所在数字的位数
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9*start*digit
        # 确定所求数位所在的数字
        num = start + (n-1) // digit
        # 确定所求数位在 num 的哪一数位
        return int(str(num)[(n - 1) % digit])


def offer_(n):
    """"""
    solution = Solution()
    output = solution.findNthDigit(n)

    print(output)


if __name__ == '__main__':
    offer_(n=3)
