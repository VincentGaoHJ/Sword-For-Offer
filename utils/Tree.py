# coding=utf-8
"""
@Time   : 2020/8/2  21:52 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 
"""

from utils.Node import TreeNode as BinaryTree


def initiate_tree_structure(value_lst):
    """

    :param value_lst: [List]
    :return:
    """
    if len(value_lst) != 7:
        raise Exception("The length of three level full binary tree is seven, please check again.")
    TreeNodeLst = []
    for idx, value in enumerate(value_lst):
        # print(f'Add Node: {value}')
        if value == 'null':
            TreeNodeLst.append('null')
        else:
            TreeNodeLst.append(BinaryTree(value))

    for node_inx in range(3):
        if TreeNodeLst[2 * node_inx + 1] != 'null':
            TreeNodeLst[node_inx].left = TreeNodeLst[2 * node_inx + 1]
        if TreeNodeLst[2 * node_inx + 2] != 'null':
            TreeNodeLst[node_inx].right = TreeNodeLst[2 * node_inx + 2]

    print('Pro-order Traverse:', end=' ')
    traverse_tree(TreeNodeLst[0])
    print('*' * 10, 'Finish Init', '*' * 10)
    return TreeNodeLst[0]


def traverse_tree(head_node):
    """
    :param head_node: [TreeNode]
    :return:
    """
    if head_node is None:
        return
    print(head_node.val, end=' ')
    traverse_tree(head_node.left)
    traverse_tree(head_node.right)
