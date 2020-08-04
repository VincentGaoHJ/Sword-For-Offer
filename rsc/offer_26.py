# coding=utf-8
"""
@Time   : 2020/8/2  21:28 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 26. 树的子结构
    https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/
"""

from utils.Node import TreeNode


class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        # 如果有一个为空（也就是A为空，因为B不发生变化），那么就说明遍历完了还没有找到子树
        if (A == None or B == None):
            return False
        # 如果直接给的 A B 两棵树满足条件，直接返回True
        if self.judge_tree(A, B):
            return True
        # 递归开始判断左子树和右子树
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def judge_tree(self, A, B):
        # b都遍历完了，还没发现不一样的，说明那就一样了
        if not B:
            return True
        # 压根就没有a，当然不行
        if not A:
            return False
        # a b 的值不相等，肯定不行
        if A.val != B.val:
            return False
        # 开始遍历两个树结构的左子树和右子树判断是否一致
        return self.judge_tree(A.left, B.left) and self.judge_tree(A.right, B.right)


def initiate_tree_structure():
    a_node1 = TreeNode(3)
    a_node2 = TreeNode(4)
    a_node3 = TreeNode(5)
    a_node4 = TreeNode(1)
    a_node5 = TreeNode(2)

    a_node1.left = a_node2
    a_node1.right = a_node3
    a_node2.left = a_node4
    a_node2.right = a_node5

    b_node1 = TreeNode(4)
    b_node2 = TreeNode(1)

    b_node1.left = b_node2

    return a_node1, b_node1


def offer_26():
    """
    输入两棵二叉树 A 和 B，判断 B 是不是 A 的子结构。(约定空树不是任意一个树的子结构)
    B 是 A 的子结构， 即 A 中有出现和 B 相同的结构和节点值。
    给定的树 A:
         3
        / \
       4   5
      / \
     1   2
    给定的树 B：
       4 
      /
     1
    返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
    输入：A = [3,4,5,1,2], B = [4,1]
    输出：true
    限制：0 <= 节点个数 <= 10000
    :return:
    """

    root_a, root_b = initiate_tree_structure()

    solution = Solution()
    output = solution.isSubStructure(root_a, root_b)

    print(output)


# 先序遍历树 A 中的每个节点 n_A
# 判断树 A 中 以 n_A 为根节点的子树 是否包含树 B

if __name__ == '__main__':
    # 剑指 Offer 26. 树的子结构
    offer_26()
