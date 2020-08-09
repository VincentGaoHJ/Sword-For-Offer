# coding=utf-8
"""
@Time   : 2020/8/9  11:20 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 24. 反转链表
    https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
"""

from utils.LinkList import SingleLinkList, printSingleLinkList
from utils.Node import ListNode


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head

        node_lst = []
        while head:
            tmp_node = ListNode(head.val)
            head = head.next
            if not node_lst:
                tmp_node.next = None
                node_lst.append(tmp_node)
            else:
                tmp_node.next = node_lst[-1]
                node_lst.append(tmp_node)

        return node_lst[-1]


def offer_24(value_lst):
    """
    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
    限制：0 <= 节点个数 <= 5000
    :param value_lst:
    :return:
    """

    sll = SingleLinkList()
    for node_value in value_lst:
        sll.append(node_value)
    head_node = sll._SingleLinkList__head
    printSingleLinkList(head_node)

    solution = Solution()
    output = solution.reverseList(head_node)

    printSingleLinkList(output)


if __name__ == '__main__':
    # 剑指 Offer 24. 反转链表
    offer_24([1, 2, 3, 4, 5])
    offer_24([])
