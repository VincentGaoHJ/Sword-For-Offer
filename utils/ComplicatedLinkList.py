# coding=utf-8
"""
@Time   : 2020/8/10  11:12 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 
"""

from utils.SingleLinkList import printSingleLinkList
from utils.Node import ComplicatedNode as Node


def ComplicatedLinkList(value_2d_lst):
    """

    :param value_2d_lst:
    :return:
    """
    if not value_2d_lst: return None
    node_lst = [Node(value) for value, _ in value_2d_lst]

    for idx, [_, random] in enumerate(value_2d_lst):
        node_lst[idx].next = node_lst[idx + 1] if idx is not len(node_lst) - 1 else None
        node_lst[idx].random = node_lst[random] if random != 'null' else None

    return node_lst[0]


if __name__ == '__main__':
    head = ComplicatedLinkList([[7, 'null'], [13, 0], [11, 4], [10, 2], [1, 0]])
    printSingleLinkList(head)
