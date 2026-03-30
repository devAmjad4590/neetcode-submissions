class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row checker
        for i in range(len(board)):
            num = set()
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in num:
                    return False
                num.add(board[i][j])

        # column checker
        for i in range(len(board)):
            num = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] in num:
                    return False
                num.add(board[j][i])
        # 3 by 3 checker9
        for square in range(len(board)):
            num = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in num:
                        return False
                    num.add(board[row][col])
        return True

        