# coding=utf-8
"""
@Time   : 2020/11/28  11:43 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Reverse Nodes in k-Group
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        NodeHead = NodeCurr = head
        flag = 0
        while head:
            flag += 1
            if flag == 1:
                tmpHead = head
            if flag == k:
                flag = 0
                tmpHead, tmpTail = self.reverseListK(tmpHead, k)
                NodeCurr.next = tmpHead
                NodeCurr = tmpTail
            head = head.next
        if flag != 0:
            NodeCurr.next = tmpHead
        return NodeHead.next

    def reverseListK(self, head, k):
        reverse_head = reverse_tail = ListNode(head.val)
        head = head.next
        num = 1
        while head and num < k:
            num += 1
            tmpNode = ListNode(head.val)
            tmpNode.next = reverse_head
            reverse_head = tmpNode
            head = head.next
        return reverse_head, reverse_tail

# Reverse Nodes in k-Group

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes,
# in the end, should remain as it is.
