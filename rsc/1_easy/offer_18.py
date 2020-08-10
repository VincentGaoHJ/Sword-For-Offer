# coding=utf-8
"""
@Time   : 2020/8/9  16:21 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 18. 删除链表的节点
    https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
"""

from utils.Node import ListNode
from utils.SingleLinkList import SingleLinkList, printSingleLinkList


class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur = head
        if cur.val == val: return cur.next
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return head
            cur = cur.next
        return head

    def deleteNode_alter(self, head, val):
        """更优雅的办法就是用递归，将所有情况都归结为一种：处理删除头结点问题"""
        if head.val == val:
            return head.next
        head.next = self.deleteNode(head.next, val)
        return head


def offer_18(value_lst, val):
    """
    给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
    返回删除后的链表的头节点。
    说明：题目保证链表中节点的值互不相同
    :param value_lst:
    :param val:
    :return:
    """
    sll = SingleLinkList()
    for node_value in value_lst:
        sll.append(node_value)
    head_node = sll._SingleLinkList__head
    printSingleLinkList(head_node)

    solution = Solution()
    output_1 = solution.deleteNode(head_node, val)
    output_2 = solution.deleteNode_alter(head_node, val)
    printSingleLinkList(output_1)
    printSingleLinkList(output_2)


if __name__ == '__main__':
    # 剑指 Offer 18. 删除链表的节点

    # Output: [5,-99]
    offer_18(value_lst=[-3, 5, -99], val=-3)

    # Output: [4,1,9]
    # 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
    offer_18(value_lst=[4, 5, 1, 9], val=5)

    # Output: [4,5,9]
    # 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
    offer_18(value_lst=[4, 5, 1, 9], val=1)
