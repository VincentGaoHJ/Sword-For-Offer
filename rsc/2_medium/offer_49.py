# coding=utf-8
"""
@Time   : 2020/10/24  11:28 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 49. 丑数
    https://leetcode-cn.com/problems/chou-shu-lcof/
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
            if dp[i] == dp[a] * 2:
                a += 1
            if dp[i] == dp[b] * 3:
                b += 1
            if dp[i] == dp[c] * 5:
                c += 1
        return dp[-1]


def offer_49(n):
    """
    我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
    :param n:
    :return:
    """
    solution = Solution()
    output = solution.nthUglyNumber(n)

    print(output)


# 每轮计算 dp[i]dp[i] 后，需要更新索引 a, b, ca,b,c 的值，使其始终满足方程条件。
# 实现方法：分别独立判断 dp[i] 和 dp[a]×2 , dp[b]×3 , dp[c]×5 的大小关系，若相等则将对应索引 a , b , c 加 1 。
if __name__ == '__main__':
    # 剑指 Offer 49. 丑数

    # 输出: 12
    # 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
    offer_49(10)
