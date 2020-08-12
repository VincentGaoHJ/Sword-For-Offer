# coding=utf-8
"""
@Time   : 2020/8/1  19:46 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 各式各样的节点类
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a Complicated Node.
class ComplicatedNode:
    def __init__(self, x, next=None, random=None):
        """
        在复杂链表中，每个节点除了有一个 next 指针指向下一个节点
        还有一个 random 指针指向链表中的任意节点或者 null。
        """
        self.val = int(x)
        self.next = next
        self.random = random
