# coding=utf-8
"""
@Time   : 2020/8/6  16:40 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 20. 表示数值的字符串
    https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/
"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0:
            print('[FALSE] There is no substantive content.')
            return False
        met_dot = met_e = met_num = False
        for idx, char in enumerate(s):
            if char in ['+', '-']:
                if idx > 0 and s[idx - 1] not in ['e', 'E']:
                    print('[FALSE] +/- is not in the beginning.')
                    return False
            elif char == '.':
                if met_dot or met_e:
                    print('[FALSE] There are more than one "." in the string, or "e/E" before the dot.')
                    return False
                met_dot = True
            elif char in ['e', 'E']:
                if met_e or not met_num:
                    print('[FALSE] There are more than one "e/E" in the string, or no digit before e/E.')
                    return False
                met_e = True
            elif char.isdigit():
                met_num = True
            else:
                print('[FALSE] There are something other than digital/e/E/./+/- in the string: {}'.format(char))
                return False

        if s.endswith('e') or s.endswith('E') or s.endswith('+') or s.endswith('-'):
            print('[FALSE] e/E/+/- should not be the last thing in the string')
            return False

        if met_dot and not met_num:
            print('[FALSE] There is no valid digit but a dot.')
            return False
        return True


def offer_20(input_str):
    """
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
    例如，字符串 "+100"、"5e2"、"-123"、"3.1416"、"0123" 都表示数值，
    但 "12e"、"1a3.14"、"1.2.3"、"+-5"、"-1E-16" 及 "12e+5.4" 都不是。
    :param input_str: [str]
    :return:
    """
    print('*' * 10, input_str, '*' * 10)
    solution = Solution()
    output = solution.isNumber(input_str)
    print(output)


if __name__ == '__main__':
    # 剑指 Offer 20. 表示数值的字符串
    offer_20('+100')  # True
    offer_20('5e2')  # True
    offer_20('-123')  # True
    offer_20('3.1416')  # True
    offer_20('0123')  # True
    offer_20(' 005047e+6')  # True

    offer_20('12e')  # False
    offer_20('1a3.14')  # False
    offer_20('1.2.3')  # False
    offer_20('+-5')  # False
    offer_20('-1E-16')  # False
    offer_20('12e+5.4')  # False
