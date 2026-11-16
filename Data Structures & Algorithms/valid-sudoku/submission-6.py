class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            for col in range(9):
                a = board[row][col]

                if a != ".":
                    if a in rows[row] or a in cols[col] or a in squares[(row//3),(col//3)]:
                        return False
                    rows[row].add(a)
                    cols[col].add(a)
                    squares[(row//3),(col//3)].add(a)
        return True