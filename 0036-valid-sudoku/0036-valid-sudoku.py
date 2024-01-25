class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=collections.defaultdict(set) # Create HashSet for every row and col and check if the element exists or not in this row and colms.
        rows=collections.defaultdict(set)
        squares=collections.defaultdict(set) # for 0 to 8 when we divide an element with 3 we get a value of 0 to 2, according to that we can store elements in a hash map example for squares[0][1] we can save a list of elements which can be 1 to 9 without repeating themselves.  
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3),(c//3)].add(board[r][c])
        return True
                    
