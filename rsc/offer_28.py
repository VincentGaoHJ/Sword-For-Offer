# coding=utf-8
"""
@Time   : 2020/8/6  14:32 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 28. 对称的二叉树
    https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/
"""

from utils.Node import TreeNode
from utils.Tree import initiate_tree_structure


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recur(root.left, root.right) if root else True

    def recur(self, left_tree, right_tree):
        """交叉递归"""
        # 两边都没有子节点了，说明同时遍历完了两个对称的支路，返回 True
        if not left_tree and not right_tree:
            return True
        # 如果一边已经遍历完了，另一边没有，则返回 False
        if not left_tree or not right_tree:
            return False
        # 如果两边都有节点，但是节点的值不相同，则返回 False
        if left_tree.val != right_tree.val:
            return False
        # 以上情况都不存在的话，说明至少到现在两边都一直，那么就看看两边的两路子路是否相同
        return self.recur(left_tree.right, right_tree.left) and self.recur(left_tree.left, right_tree.right)


def offer_28(input_lst):
    """
    请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
    例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
        1
       / \
      2   2
       \   \
       3    3
    输入：root = [1,2,2,3,4,4,3]
    输出：true
    输入：root = [1,2,2,null,3,null,3]
    输出：false
    限制：0 <= 节点个数 <= 1000
    :return:
    """
    headNode = initiate_tree_structure(input_lst)
    solution = Solution()
    output = solution.isSymmetric(headNode)
    print(output)


if __name__ == '__main__':
    # 剑指 Offer 28. 对称的二叉树
    offer_28([1, 2, 2, 3, 4, 4, 3])
    offer_28([1, 2, 2, 'null', 3, 'null', 3])
    offer_28([2, 3, 3, 4, 5, 5, 4])
    offer_28([2, 3, 3, 4, 5, 5, 'null'])
