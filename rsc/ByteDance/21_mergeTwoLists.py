# coding=utf-8
"""
@Time   : 2020/11/27  15:44 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Merge Two Sorted Lists
    https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newListHead = newListNode = ListNode()
        while l1 or l2:
            value1 = l1.val if l1 else None
            value2 = l2.val if l2 else None
            if value1 is None and value2 is None:
                break
            elif value1 is None and value2 is not None:
                tmpNode = ListNode(value2)
                l2 = l2.next
            elif value1 is not None and value2 is None:
                tmpNode = ListNode(value1)
                l1 = l1.next
            else:
                if value1 <= value2:
                    tmpNode = ListNode(value1)
                    l1 = l1.next
                else:
                    tmpNode = ListNode(value2)
                    l2 = l2.next
            newListNode.next = tmpNode
            newListNode = newListNode.next
        return newListHead.next

# Merge Two Sorted Lists