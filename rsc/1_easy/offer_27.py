# coding=utf-8
"""
@Time   : 2020/8/4  21:55 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 27. 二叉树的镜像
    https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
"""

from utils.Node import TreeNode


class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return
        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)

        return root


def offer_27():
    """
    请完成一个函数，输入一个二叉树，该函数输出它的镜像。
    例如输入：
         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    镜像输出：
         4
       /   \
      7     2
     / \   / \
    9   6 3   1
    :return:
    """

    root = initiate_tree_structure()

    solution = Solution()
    output = solution.mirrorTree(root)

    print(output.val)


def initiate_tree_structure():
    a_node1 = TreeNode(4)
    a_node2 = TreeNode(2)
    a_node3 = TreeNode(7)
    a_node4 = TreeNode(1)
    a_node5 = TreeNode(3)
    a_node6 = TreeNode(6)
    a_node7 = TreeNode(9)

    a_node1.left = a_node2
    a_node1.right = a_node3
    a_node2.left = a_node4
    a_node2.right = a_node5
    a_node3.left = a_node6
    a_node3.right = a_node7

    return a_node1


# 根据二叉树镜像的定义，考虑递归遍历（dfs）二叉树，
# 交换每个节点的左 / 右子节点，即可生成二叉树的镜像。
if __name__ == '__main__':
    # 剑指 Offer 27. 二叉树的镜像
    offer_27()
