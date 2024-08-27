class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        OCount = 0
        XCount = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == "O":
                    OCount += 1
                elif board[i][j] == "X":
                    XCount += 1
        if XCount < OCount or XCount - OCount > 1:
            return False

        def check_win_positions(board, player):
            for i in range(len(board)):
                if board[i][0] == board[i][1] == board[i][2] == player:
                    return True                        
            for i in range(len(board)):
                if board[0][i] == board[1][i] == board[2][i] == player:
                    return True 				
            if board[0][0] == board[1][1] == board[2][2]  == player or \
                board[0][2] == board[1][1] == board[2][0] == player:
                return True
                            
            return False
        
        if check_win_positions(board, "X") and XCount != OCount + 1:
            return False
        if check_win_positions(board, "O"):
            if check_win_positions(board, "X"):
                return False
            return OCount == XCount

        return True
        