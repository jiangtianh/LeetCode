class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = [set() for _ in range(9)]
        vertical = [set() for _ in range(9)]
        block = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] not in horizontal[row]:
                        horizontal[row].add(board[row][col])
                    else:
                        return False 
                    if board[row][col] not in vertical[col]:
                        vertical[col].add(board[row][col])
                    else:
                        return False 

                    cubeIdx = row // 3 * 3 + col // 3
                    if board[row][col] not in block[cubeIdx]:
                        block[cubeIdx].add(board[row][col])
                    else:
                        return False
                    
        return True