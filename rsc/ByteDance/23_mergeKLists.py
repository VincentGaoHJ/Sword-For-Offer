# coding=utf-8
"""
@Time   : 2020/11/29  16:07 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from Queue import PriorityQueue


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        headNode = curr = ListNode(None)
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put([node.val, node])
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next:
                q.put([curr.next.val, curr.next])
        return headNode.next
