# coding=utf-8
"""
@Time   : 2020/12/4  16:40 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Optimal Account Balancing
    https://leetcode-cn.com/problems/optimal-account-balancing/
"""


class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        count_balance = {}
        for x, y, z in transactions:
            count_balance[x] = z if not count_balance.get(x) else count_balance[x] + z
            count_balance[y] = -z if not count_balance.get(y) else count_balance[y] - z
        balance_lst = count_balance.values()
        return self.dfs(balance_lst)

    def dfs(self, balance_lst):
        balance_lst = [i for i in balance_lst if i != 0]
        if not balance_lst:
            return 0
        for value in balance_lst:
            if -value in balance_lst:
                balance_lst.remove(value)
                balance_lst.remove(-value)
                return self.dfs(balance_lst) + 1
        trans_lst = []
        for i in range(len(balance_lst)):
            for j in range(i + 1, len(balance_lst)):
                balance_lst_tmp = balance_lst[:]
                if balance_lst[i] * balance_lst[j] < 0:
                    balance_lst_tmp[j] = balance_lst_tmp[i] + balance_lst_tmp[j]
                    balance_lst_tmp[i] = 0
                    trans_lst.append(self.dfs(balance_lst_tmp))
        return min(trans_lst) + 1


def solution(transactions):
    """
    A group of friends went on holiday and sometimes lent each other money.
    For example, Alice paid for Bill's lunch for $10.
    Then later Chris gave Alice $5 for a taxi ride.
    We can model each transaction as a tuple (x, y, z) which means person x gave person y $z.
    Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID),
    the transactions can be represented as [[0, 1, 10], [2, 0, 5]].
    Given a list of transactions between a group of people,
    return the minimum number of transactions required to settle the debt.
    Note:
    A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
    Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
    Example 1:
    Input:
    [[0,1,10], [2,0,5]]
    Output:
    2
    Explanation:
    Person #0 gave person #1 $10.
    Person #2 gave person #0 $5.
    Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
    Example 2:
    Input:
    [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
    Output:
    1
    Explanation:
    Person #0 gave person #1 $10.
    Person #1 gave person #0 $1.
    Person #1 gave person #2 $5.
    Person #2 gave person #0 $5.
    Therefore, person #1 only need to give person #0 $4, and all debt is settled.
    :param transactions:
    :return:
    """
    solution = Solution()
    output = solution.minTransfers(transactions)

    print(output)


if __name__ == '__main__':
    # Optimal Account Balancing
    solution([[10, 11, 6], [12, 13, 7], [14, 15, 2], [14, 16, 2], [14, 17, 2], [14, 18, 2]])
