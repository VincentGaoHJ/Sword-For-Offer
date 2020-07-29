# coding=utf-8
"""
@Time   : 2020/7/30  0:35 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 剑指 Offer 12. 矩阵中的路径
    https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        visited_array = [[0] * len(board[0]) for _ in range(len(board))]
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if self.search(row, col, rows, cols, board, word, visited_array):
                    return True
        return False

    def search(self, row, col, rows, cols, board, word, visited_array):
        if not word:
            return True
        has_path = False
        if 0 <= col < cols and 0 <= row < rows and (not visited_array[row][col]) and (word[0] == board[row][col]):
            visited_array[row][col] = 1
            has_path = self.search(
                row + 1, col, rows, cols, board, word[1:], visited_array) or self.search(
                row - 1, col, rows, cols, board, word[1:], visited_array) or self.search(
                row, col + 1, rows, cols, board, word[1:], visited_array) or self.search(
                row, col - 1, rows, cols, board, word[1:], visited_array)
            if not has_path:
                visited_array[row][col] = 0
        return has_path


def offer_12():
    """

    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
    路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
    如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
    例如，在下面的 3×4 的矩阵中包含一条字符串 “bfce” 的路径（路径中的字母用加粗标出）。

    [["a","b","c","e"],
    ["s","f","c","s"],
    ["a","d","e","e"]]

    但矩阵中不包含字符串 “abfb” 的路径，因为字符串的第一个字符 b 占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    输出：true
    输入：board = [["a","b"],["c","d"]], word = "abcd"
    输出：false
    提示：
        1 <= board.length <= 200
        1 <= board[i].length <= 200

    :return:
    """

    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"

    solution = Solution()
    is_path = solution.exist(board, word)

    print(is_path)


# 主程序寻找起点，辅助函数用于在给定起点和已探测节点的基础上继续 DFS 探测
# 用一个字典保留已探测的节点避免重复探测。
# 当探测节点个数等于目标字符串长度时，即可返回；否则回溯至上一节点。

if __name__ == '__main__':
    # 剑指 Offer 12. 矩阵中的路径
    offer_12()
