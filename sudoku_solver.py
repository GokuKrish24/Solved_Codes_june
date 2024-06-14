def solveSudoku(board):
        def check(k,board,row,col):
            for i in range(9):
                if(board[i][col]==k):
                    return False
                if(board[row][i]==k):
                    return False
                if(board[3*(row//3)+i//3][3*(col//3)+i%3]==k):
                    return False
            return True
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if(board[i][j]=="."):
                        for k in range(1,10):
                            if(check(str(k),board,i,j)):
                                board[i][j]=str(k)
                                if(solve(board)):
                                    return True
                                board[i][j]="."
                        return False
            return True
        solve(board)
