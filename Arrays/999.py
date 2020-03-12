class Solution:
    """
    Time 74% (28ms)
    """
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return self.check_directions(i,j,board)

    # Check all directions and return sum
    def check_directions(self,i,j,board):
        return self.check_up(i,j,board) + self.check_down(i,j,board) + self.check_left(i,j,board) + self.check_right(i,j,board)
    
    def check_up(self,i,j,board):
        i = i - 1
        while i >= 0:
            if board[i][j] == 'p':
                return 1
            elif board[i][j] == 'B':
                return 0
            i -= 1
        return 0

    def check_down(self,i,j,board):
        i = i + 1
        while i < 8:
            if board[i][j] == 'p':
                return 1
            elif board[i][j] == 'B':
                return 0
            i += 1
        return 0

    def check_left(self,i,j,board):
        j = j - 1
        while j >= 0:
            if board[i][j] == 'p':
                return 1
            elif board[i][j] == 'B':
                return 0
            j -= 1
        return 0

    def check_right(self,i,j,board):
        j = j + 1
        while j < 8:
            if board[i][j] == 'p':
                return 1
            elif board[i][j] == 'B':
                return 0
            j += 1
        return 0
