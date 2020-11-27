# coding=utf-8
"""
@Time   : 2020/10/22  10:23 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch :
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_str = ''
        tmp_tail = -1
        for i in range(len(s)):
            if i < tmp_tail:
                continue
            center_head, center_tail = i, i
            while center_tail < len(s) and s[center_head] == s[center_tail]:
                tmp_str = self.find_longest(s, center_head, center_tail)
                if len(tmp_str) >= len(longest_str):
                    longest_str = tmp_str
                center_tail += 1
            tmp_tail = center_tail
        return longest_str

    def find_longest(self, s, center_head, center_tail):
        while center_head - 1 >= 0 and center_tail + 1 < len(s):
            if s[center_head - 1] != s[center_tail + 1]:
                return s[center_head:center_tail + 1]
            else:
                center_head -= 1
                center_tail += 1
        return s[center_head:center_tail + 1]


def solution(s):
    """"""
    solution = Solution()
    output = solution.longestPalindrome(s)

    print(output)


if __name__ == '__main__':
    solution(s="babad")
    solution(s="a")
    solution(s="aba")
    solution(s="cbbd")
