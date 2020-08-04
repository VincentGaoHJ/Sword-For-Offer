# coding=utf-8
"""
@Time   : 2020/8/2  21:52 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 
"""

from utils.Node import TreeNode as BinaryTree


# 二叉树类
class BinaryTree(object):
    # 初始化，传入根节点的值
    def __init__(self, root_value):
        self.root = root_value
        self.leftchild = None
        self.rightchild = None

    # 插入左子树
    def insert_left(self, left_value):
        if self.leftchild == None:
            self.leftchild = BinaryTree(left_value)
        else:
            left_subtree = BinaryTree(left_value)
            left_subtree.leftchild = self.leftchild
            self.leftchild = left_subtree

    # 插入右子树
    def insert_right(self, right_value):
        if self.rightchild == None:
            self.rightchild = BinaryTree(right_value)
        else:
            right_subtree = BinaryTree(right_value)
            right_subtree.rightchild = self.rightchild
            self.rightchild = rightchild

    # 设置根节点的值
    def set_root(self, root_value):
        self.root = root_value

    # 获取根节点的值
    def get_root(self):
        return self.root

    # 获取左子树
    def get_leftchild(self):
        return self.leftchild

    # 获取右子树
    def get_rightchile(self):
        return self.rightchild
