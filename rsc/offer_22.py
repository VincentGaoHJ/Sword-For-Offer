# coding=utf-8
"""
@Time   : 2020/8/7  10:43 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 22. 链表中倒数第 k 个节点
    https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
"""

from utils.LinkList import SingleLinkList, printSingleLinkList
from utils.Node import ListNode


class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node_pointer_a = node_pointer_b = head
        idx_b = 0
        while node_pointer_b:
            node_pointer_b = node_pointer_b.next
            if idx_b < k:
                idx_b += 1
            else:
                node_pointer_a = node_pointer_a.next
        return node_pointer_a


def offer_22(lst, k):
    """
    输入一个链表，输出该链表中倒数第 k 个节点。
    为了符合大多数人的习惯，本题从 1 开始计数，即链表的尾节点是倒数第 1 个节点。
    例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。
    这个链表的倒数第 3 个节点是值为 4 的节点。

    给定一个链表: 1->2->3->4->5, 和 k = 2.
    返回链表 4->5.
    :param lst:
    :param k:
    :return:
    """
    sll = SingleLinkList()
    for node_value in lst:
        sll.append(node_value)
    headNode = sll._SingleLinkList__head
    printSingleLinkList(headNode)
    solution = Solution()
    output_node = solution.getKthFromEnd(headNode, k)
    printSingleLinkList(output_node)


if __name__ == '__main__':
    # 剑指 Offer 22. 链表中倒数第 k 个节点
    offer_22([1, 2, 3, 4, 5], 2)
