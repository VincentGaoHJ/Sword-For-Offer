# coding=utf-8
"""
@Time   : 2020/7/23  19:27 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 09. 用两个栈实现队列
    https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
"""


class CQueue(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """

        self.stack_1.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.stack_2:
            return self.stack_2.pop()

        if not self.stack_1:
            return -1

        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())

        return self.stack_2.pop()


def offer_09():
    """
    用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
    分别完成在队列尾部插入整数和在队列头部删除整数的功能。
    (若队列中没有元素，deleteHead 操作返回 -1 )

    输入：
    ["CQueue","appendTail","deleteHead","deleteHead"]
    [[],[3],[],[]]
    输出：[null,null,3,-1]

    提示：
    1 <= values <= 10000
    最多会对 appendTail、deleteHead 进行 10000 次调用

    :return:
    """

    inputs = ["CQueue", "appendTail", "deleteHead", "deleteHead"]
    value = [[], [3], [], []]

    for index, (input_operation, input_value) in enumerate(zip(inputs, value)):
        if input_operation == "CQueue":
            obj = CQueue()
            print([])
        elif input_operation == "appendTail":
            obj.appendTail(input_value[0])
            print([])
        elif input_operation == "deleteHead":
            param_2 = obj.deleteHead()
            print(param_2)


if __name__ == '__main__':
    # 剑指 Offer 09. 用两个栈实现队列
    offer_09()
