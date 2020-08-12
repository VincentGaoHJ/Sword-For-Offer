# coding=utf-8
"""
@Time   : 2020/8/10  11:01 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 35. 复杂链表的复制
    https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
"""

from utils.Node import ComplicatedNode as Node
from utils.SingleLinkList import printSingleLinkList
from utils.ComplicatedLinkList import ComplicatedLinkList


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        visited = {}
        new_head, visited = self.depth_first_search(head, visited)
        return new_head

    def depth_first_search(self, head, visited):
        if not head:
            return None, visited
        if head in visited:
            return visited[head], visited
        new_node = Node(head.val)
        visited[head] = new_node
        new_node.next, visited = self.depth_first_search(head.next, visited)
        new_node.random, visited = self.depth_first_search(head.random, visited)
        return new_node, visited


def offer_35(value_2d_lst):
    """
    请实现 copyRandomList 函数，复制一个复杂链表。
    在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
    :param value_2d_lst: 
    :return: 
    """
    head = ComplicatedLinkList(value_2d_lst)
    printSingleLinkList(head)

    solution = Solution()
    output_node = solution.copyRandomList(head)

    if output_node:
        print(output_node.val)

    printSingleLinkList(output_node)


if __name__ == '__main__':
    # 剑指 Offer 35. 复杂链表的复制

    # 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
    offer_35([[7, 'null'], [13, 0], [11, 4], [10, 2], [1, 0]])

    # 输出：[[1,1],[2,1]]
    offer_35([[1, 1], [2, 1]])

    # 输出：[[3,null],[3,0],[3,null]]
    offer_35([[3, 'null'], [3, 0], [3, 'null']])

    # 输出：[]
    # 解释：给定的链表为空（空指针），因此返回 null。
    offer_35([])
