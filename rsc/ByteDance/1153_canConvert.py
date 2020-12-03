# coding=utf-8
"""
@Time   : 2020/12/3  19:44 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : String Transforms Into Another String
    https://leetcode-cn.com/problems/string-transforms-into-another-string/
"""


class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        hash_map = {}
        for s1, s2 in zip(str1, str2):
            if s1 in hash_map:
                if hash_map[s1] != s2:
                    return False
            else:
                hash_map[s1] = s2
        value = set(hash_map.values())
        if len(value) == 26 and str1 != str2:
            return False
        return True


def solution(str1, str2):
    """
    Given two strings str1 and str2 of the same length,
    determine whether you can transform str1 into str2 by doing zero or more conversions.
    In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.
    Return true if and only if you can transform str1 into str2.
    Example 1:
    Input: str1 = "aabcc", str2 = "ccdee"
    Output: true
    Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
    Example 2:
    Input: str1 = "leetcode", str2 = "codeleet"
    Output: false
    Explanation: There is no way to transform str1 to str2.
    Note:
    1 <= str1.length == str2.length <= 10^4
    Both str1 and str2 contain only lowercase English letters.
    :return:
    """
    solution = Solution()
    output = solution.canConvert(str1, str2)

    print(output)


if __name__ == '__main__':
    # String Transforms Into Another String
    solution(str1="leetcode", str2="codeleet")
