class ConnectFour:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.player = 'X'

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 13)

    def make_move(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.player
                return True
        return False

    def check_win(self):
        # Check rows
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == self.player and all(
                        self.board[row][col + i] == self.player for i in range(4)):
                    return True

        # Check columns
        for col in range(7):
            for row in range(3):
                if self.board[row][col] == self.player and all(
                        self.board[row + i][col] == self.player for i in range(4)):
                    return True

        # Check diagonal \
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.player and all(
                        self.board[row + i][col + i] == self.player for i in range(4)):
                    return True

        # Check diagonal /
        for row in range(3):
            for col in range(3, 7):
                if self.board[row][col] == self.player and all(
                        self.board[row + i][col - i] == self.player for i in range(4)):
                    return True

        return False

    def play_game(self):
        print("Welcome to Connect Four!")
        self.display_board()
        while True:
            try:
                column = int(input(f"Player {self.player}, enter column (0-6): "))
                if column < 0 or column > 6:
                    print("Column out of range. Please enter a number between 0 and 6.")
                    continue
                if self.make_move(column):
                    self.display_board()
                    if self.check_win():
                        print(f"Player {self.player} wins!")
                        break
                    self.player = 'O' if self.player == 'X' else 'X'
                else:
                    print("Column is full. Please choose another column.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()
