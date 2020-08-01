# coding=utf-8
"""
@Time   : 2020/8/1  19:46 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 单链表使用的节点类
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None