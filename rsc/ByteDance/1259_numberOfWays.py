# coding=utf-8
"""
@Time   : 2020/12/3  20:10 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Handshakes That Don't Cross
    https://leetcode-cn.com/problems/handshakes-that-dont-cross/
"""


class Solution(object):
    def numberOfWays(self, num_people):
        """
        :type num_people: int
        :rtype: int
        """
        sum_num = 0
        if num_people == 2:
            return 1
        remain = num_people - 2
        target = 2
        while target <= num_people:
            part_1_num = self.numberOfWays(target - 2) if target - 2 else 1
            part_2_num = self.numberOfWays(num_people - target) if num_people - target else 1
            sum_num += part_1_num * part_2_num
            target += 2
        return sum_num


def solution(num_people):
    """
    You are given an even number of people num_people that stand around a circle
    and each person shakes hands with someone else, so that there are num_people / 2 handshakes total.
    Return the number of ways these handshakes could occur such that none of the handshakes cross.
    Since this number could be very big, return the answer mod 10^9 + 7
    :param num_people:
    :return:
    """
    solution = Solution()
    output = solution.numberOfWays(num_people)

    print(output)


if __name__ == '__main__':
    # 方法并没有通过所有的测试案例
    # 尝试方向应该将递归改成状态转移
    # Handshakes That Don't Cross
    solution(6)
