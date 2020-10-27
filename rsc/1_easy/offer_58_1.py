# coding=utf-8
"""
@Time   : 2020/10/27  9:45 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 58 - I. 翻转单词顺序
    https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.strip()  # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':  # 搜索首个空格
                i -= 1
            res.append(s[i + 1:j + 1])  # 添加单词
            while s[i] == ' ':  # 跳过单词间空格
                i -= 1
            j = i  # j 指向下个单词的尾字符
        return ' '.join(res)  # 拼接并返回


def offer_58(s):
    """
    输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
    为简单起见，标点符号和普通字母一样处理。
    例如输入字符串 "I am a student."，则输出 "student. a am I"。
    :param s:
    :return:
    """
    solution = Solution()
    output = solution.reverseWords(s)

    print(output)


if __name__ == '__main__':
    # 剑指 Offer 58 - I. 翻转单词顺序
    offer_58("the sky is blue")
