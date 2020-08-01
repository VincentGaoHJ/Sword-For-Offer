# coding=utf-8
"""
@Time   : 2020/8/1  19:46 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 单链表
    https://blog.csdn.net/kang19950919/article/details/88890853
"""

from utils.Node import ListNode as Node


class LinkList(object):
    def __init__(self, node=None, *args, **kwargs):
        if node is None:
            self.__head = node
        else:
            self.__head = Node(node)
            for arg in args:
                self.append(arg)
        if kwargs.values() is not None:
            for kwarg in kwargs:
                self.append(kwargs[kwarg])

    def is_empty(self):
        """链表是否为空
        :return 如果链表为空 返回真
        """
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素
        :param item: 要保存的具体数据
        """
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        # 如果链表为空，需要特殊处理
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # 退出循环的时候，cur指向的尾结点
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 在头部添加元素
        if pos <= 0:
            self.add(item)
        # 在尾部添加元素
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 退出循环的时候，cur指向pos的前一个位置
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur is not None:
            # 找到了要删除的元素
            if cur.item == item:
                # 在头部找到了元素
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                return
            # 不是要找的元素，移动游标
            pre = cur
            cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def reveres(self):
        """反转元素节点"""
        if self.is_empty() or self.length() <= 1:
            return
        j = 0
        while j < self.length() - 1:
            cur = self.__head
            for i in range(self.length() - 1):
                cur = cur.next
                if cur.next is None:
                    x = cur.item
                    self.remove(cur.item)
                    self.insert(j, x)
            j += 1
