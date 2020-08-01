# coding=utf-8
"""
@Time   : 2020/8/1  20:35 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 07. 重建二叉树
    https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
"""


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        pass


def offer_07():
    """
    输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
    返回如下的二叉树：
        3
       / \
      9  20
        /  \
       15   7
    限制：0 <= 节点个数 <= 5000
    :return:
    """

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    solution = Solution()
    TreeNode = solution.buildTree(preorder, inorder)


# 根据子树特点，我们可以通过同样的方法对左（右）子树进行划分，每轮可确认三个节点的关系 。
# 此递推性质让我们联想到用 递归方法 处理。
if __name__ == '__main__':
    # 剑指 Offer 07. 重建二叉树
    offer_07()
