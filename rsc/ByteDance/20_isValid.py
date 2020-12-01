# coding=utf-8
"""
@Time   : 2020/11/29  16:23 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : Valid Parentheses
    https://leetcode-cn.com/problems/valid-parentheses/
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        chara_lst = [['(', ')'], ['{', '}'], ['[', ']']]
        for idx in range(1, len(s)):
            if [s[idx - 1], s[idx]] in chara_lst:
                s = s[:idx - 1] + s[idx + 1:]
                return self.isValid(s)
        return False


class Solution_2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren_pair = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for chara in s:
            if chara in paren_pair.values():
                stack.append(chara)
            elif chara in paren_pair and stack:
                if stack.pop() != paren_pair.get(chara):
                    return False
            else:
                return False
        if not stack:
            return True
        else:
            return False


def solution(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    :param s:
    :return:
    """
    solution = Solution()
    output = solution.isValid(s)

    print(output)

    solution = Solution_2()
    output = solution.isValid(s)

    print(output)


if __name__ == '__main__':
    # Valid Parentheses
    solution(s="()")
