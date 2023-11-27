from collections import defaultdict as dd
class Solution:
    def isValidSudoku(self, board:[[str]]) -> bool:

        rows = dd(set)
        cols = dd(set)
        sq = dd(set) # key (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in sq[r//3, c//3]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sq[(r//3,c//3)].add(board[r][c])

        return True

