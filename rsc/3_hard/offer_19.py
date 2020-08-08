# coding=utf-8
"""
@Time   : 2020/8/8  11:58 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 19. 正则表达式匹配
    https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        # 判断是否有 s 并且是否首位匹配
        first_match = bool(s) and p[0] in (".", s[0])
        # 第二位是 * 的情况
        if len(p) >= 2 and p[1] == '*':
            # 如果首位匹配，那么可以配也可以不配
            if first_match:
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            # 首位不匹配，那么只能更新 p 来继续匹配
            return self.isMatch(s, p[2:])
        # 第二位不是 * 的情况，如果首位匹配继续看，不匹配就返回 False
        return first_match and self.isMatch(s[1:], p[1:])


def offer_19(s, p):
    """
    请实现一个函数用来匹配包含'. ' 和'*' 的正则表达式。模式中的字符'.' 表示任意一个字符，而'*' 表示它前面的字符可以出现任意次（含 0 次）。
    在本题中，匹配是指字符串的所有字符匹配整个模式。
    例如，字符串 "aaa" 与模式 "a.a" 和 "ab*ac*a" 匹配，但与 "aa.a" 和 "ab*a" 均不匹配。
    :param s:
    :param p:
    :return:
    """
    solution = Solution()
    output = solution.isMatch(s, p)
    print(output)


# 递归的思路：
# 当连 x 都匹配不上时自然就是整个 X* 抛弃掉
# 当 x 匹配上时，要么抵消掉一个 s X* 保留， 要么整个 X* 抛弃掉

# 之前错误的逻辑就是思考了很多中间结果，这样的话就会徒增很多判断，并且会考虑不清楚
# 最理想的状态就是把所有可能归结为两种，然后在终点等待，最后剩下的情况再进行逐一分析
# 不要试图在过程中思考如何 return ，应该能调用递归就递归，能放到递归里的就不要 if return。
if __name__ == '__main__':
    # 剑指 Offer 19. 正则表达式匹配

    # 输出: false
    offer_19("a", ".*..a*")

    # 输出: true
    # 解释: "a" 无法匹配 "aa" 整个字符串。
    offer_19("aaa", "a*a")

    # 输出: false
    # 解释: "a" 无法匹配 "aa" 整个字符串。
    offer_19("aa", "a")

    # 输出: true
    # 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。
    # 因此，字符串 "aa" 可被视为 'a' 重复了一次。
    offer_19("aa", "a*")

    # 输出: true
    # 解释:".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
    offer_19("ab", ".*")

    # 输出: true
    # 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
    offer_19("aab", "c*a*b")

    # 输出: false
    offer_19("mississippi", "mis*is*p*.")
