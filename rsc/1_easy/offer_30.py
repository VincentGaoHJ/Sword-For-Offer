# coding=utf-8
"""
@Time   : 2020/8/13  10:02 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 30. 包含 min 函数的栈
    https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.B[-1]


def offer_30():
    """
    定义栈的数据结构
    请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中
    调用 min、push 及 pop 的时间复杂度都是 O (1)。
    :return:
    """
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(1)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.min()

    print(param_3, param_4)


# 函数设计：
# push(x) 函数： 重点为保持栈 B 的元素是 非严格降序 的
# 将 x 压入栈 A （即 A.add(x) ）
# 若 ① 栈 B 为空 或 ② x 小于等于 栈 B 的栈顶元素，则将 x 压入栈 B （即 B.add(x) ）

# pop() 函数： 重点为保持栈 A,B 的 元素一致性
# 执行栈 A 出栈（即 A.pop() ），将出栈元素记为 y
# 若 y 等于栈 B 的栈顶元素，则执行栈 B 出栈（即 B.pop() ）

# top() 函数： 直接返回栈 A 的栈顶元素即可，即返回 A.peek()

# min() 函数： 直接返回栈 B 的栈顶元素即可，即返回 B.peek()

if __name__ == '__main__':
    # 剑指 Offer 30. 包含 min 函数的栈
    offer_30()
