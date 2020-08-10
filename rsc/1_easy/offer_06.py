# coding=utf-8
"""
@Time   : 2020/8/1  16:25 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 06. 从尾到头打印链表
    https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
"""

from utils.SingleLinkList import SingleLinkList


class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        return self.reversePrint(head.next) + [head.val] if head else []


def offer_06():
    """
    输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
    输入：head = [1,3,2]
    输出：[2,3,1]
    限制：0 <= 链表长度 <= 10000
    :return:
    """

    sll = SingleLinkList()
    for node_val in [1, 3, 2]:
        sll.append(node_val)
    head_node = sll._SingleLinkList__head

    solution = Solution()
    output = solution.reversePrint(head_node)

    print(output)


# 利用递归，先走至链表末端，回溯时依次将节点值加入列表 ，这样就可以实现链表值的倒序输出。
# 递推阶段： 每次传入 head.next ，以 head == None（即走过链表尾部节点）为递归终止条件，此时返回空列表 [] 。
# 回溯阶段： 利用 Python 语言特性，递归回溯时每次返回 当前 list + 当前节点值 [head.val] ，即可实现节点的倒序输出。

if __name__ == '__main__':
    # 剑指 Offer 06. 从尾到头打印链表
    offer_06()
