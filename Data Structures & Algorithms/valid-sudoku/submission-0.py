class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isRowValid(board) and self.isColValid(board) and self.isGridValid(board)

    def isRowValid(self, board):
        for i in range(len(board)):
            uniq = set()
            for j in range(len(board[0])):
                if board[i][j] not in uniq:
                    if board[i][j].isalnum():
                        uniq.add(board[i][j])
                else:
                    print(i, j, 'row')
                    return False
        return True
    
    def isColValid(self, board):
        for i in range(len(board[0])):
            uniq = set()
            for j in range(len(board)):
                if board[j][i] not in uniq:
                    if board[j][i].isalnum():
                        uniq.add(board[j][i])
                else:
                    print(j, i, 'col')
                    return False
        return True

    def isGridValid(self, board):
        for row in range(0, len(board), 3):
            for col in range(0, len(board[0]), 3):
                uniq = set()
                for curr_row in range(row, row + 3):
                    for curr_col in range(col, col + 3):
                        if board[curr_row][curr_col] in uniq:
                            print(curr_row, curr_col, 'grid')
                            return False
                        elif board[curr_row][curr_col].isalnum():
                            uniq.add(board[curr_row][curr_col])
        return True