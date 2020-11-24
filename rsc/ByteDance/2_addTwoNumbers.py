# coding=utf-8
"""
@Time   : 2020/11/24  17:20 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        headNode = tmpNode = ListNode()
        while l1 or l2 or flag != 0:
            tmp_value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + flag
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            flag = tmp_value // 10
            tmpNode.next = ListNode(tmp_value % 10)
            tmpNode = tmpNode.next

        return headNode.next
