class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
          for j in range(9):
            val = board[i][j]
            if val == ".":
              continue
            if val in row[j] or val in col[i] or val in square[(i//3, j//3)]:
              return False
            row[j].add(val)
            col[i].add(val)
            square[(i//3, j//3)].add(val) 
        return True