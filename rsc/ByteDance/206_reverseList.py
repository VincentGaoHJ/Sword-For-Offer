# coding=utf-8
"""
@Time   : 2020/11/27  15:33 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Reverse a singly linked list.
    https://leetcode-cn.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        reverse_head = ListNode(head.val)
        head = head.next
        while head:
            tmpNode = ListNode(head.val)
            tmpNode.next = reverse_head
            reverse_head = tmpNode
            head = head.next
        return reverse_head

# Reverse a singly linked list.