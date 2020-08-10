# coding=utf-8
"""
@Time   : 2020/8/2  10:08 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 25. 合并两个排序的链表
"""

from utils.SingleLinkList import SingleLinkList, printSingleLinkList
from utils.Node import ListNode


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre_head = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return pre_head.next


def offer_25():
    """
    输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
    限制：0 <= 链表长度 <= 1000
    :return:
    """

    sll_1 = SingleLinkList()
    sll_2 = SingleLinkList()
    for node_value in [1, 2, 4]:
        sll_1.append(node_value)
    for node_value in [1, 3, 4]:
        sll_2.append(node_value)
    head_1 = sll_1._SingleLinkList__head
    head_2 = sll_2._SingleLinkList__head

    solution = Solution()
    output = solution.mergeTwoLists(head_1, head_2)
    printSingleLinkList(output)


# 初始化
# 循环合并
# 合并剩余尾部
# 返回值
if __name__ == '__main__':
    # 剑指 Offer 25. 合并两个排序的链表
    offer_25()
