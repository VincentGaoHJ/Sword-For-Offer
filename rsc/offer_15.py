# coding=utf-8
"""
@Time   : 2020/8/6  20:49 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 15. 二进制中 1 的个数
"""


class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 位运算：使用1个辅助变量依次判断各位是否为1
        flag = 1
        count = 0
        while flag <= n:
            # 对于按位与，就是对参加运算的两个整数的补码逐位进行逻辑与运算
            # 即参加运算的两个运算量，如果两个相应位都为 1，则该位的结果为 1，否则为 0。
            if flag & n:
                count += 1
            flag <<= 1
        return count

    def hamming_weight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 一个数 n 和 它-1 做与运算，就相当于干掉了最右边的 1 .
        bits = 0
        while n:
            bits += 1
            # 先假设这个数的最右边一位是 1 ，那么该数减去 1 后，最右边一位变成了 0，其他位不变；
            # 再假设最后一位不是 1 而是 0 ，而最右边的 1 在第 m 位，那么该数减去 1 ，第 m 位变成 0 ， m 右边的位变成 1 ， m 之前的位不变；
            # 上面两种情况总结，一个整数减去 1 ，都是把最右边的 1 变成 0 ，如果它后面还有 0 ，那么 0 变成 1 。
            # 那么我们把一个整数减去 1 ，与该整数做位运算，相当于把最右边的 1 变成了 0 ，比如 1100 与 1011 做位与运算，得到 1000 。
            # 那么一个整数中有多少个 1 就可以做多少次这样的运算。
            n = (n - 1) & n
        return bits


def offer_15(n):
    """
    请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。
    例如，把 9 表示成二进制是 1001，有 2 位是 1。
    因此，如果输入 9，则该函数输出 2。
    输入：00000000000000000000000000001011
    输出：3
    解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
    输入：00000000000000000000000010000000
    输出：1
    解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
    输入：11111111111111111111111111111101
    输出：31
    解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
    :param n:
    :return:
    """
    solution = Solution()
    output = solution.hammingWeight(n)
    print('solution 1: ', output)
    output = solution.hamming_weight(n)
    print('solution 2: ', output)
    pass


if __name__ == '__main__':
    offer_15(9)
