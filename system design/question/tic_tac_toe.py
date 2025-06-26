"""
Designing a Tic Tac Toe Game
Requirements
The Tic-Tac-Toe game should be played on a 3x3 grid.
Two players take turns marking their symbols (X or O) on the grid.
The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.
If all the cells on the grid are filled and no player has won, the game ends in a draw.
The game should have a user interface to display the grid and allow players to make their moves.
The game should handle player turns and validate moves to ensure they are legal.
The game should detect and announce the winner or a draw at the end of the game.
"""

class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Cell():
    def __init__(self):
        self.value = None

    def set_cell(self, value):
        self.value = value

    def is_empty(self):
        return self.value is None


class Game:
    def __init__(self, first_name, first_symbol, second_name, second_symbol, n):
        self.n = n
        self.board = [[Cell() for _ in range(n)] for _ in range(n)]
        self.first_player = Player(first_name, first_symbol)
        self.second_player = Player(second_name, second_symbol)

    def display_board(self):
        for row in self.board:
            print(" | ".join(cell.value if cell.value is not None else "_" for cell in row))
            print("-" * (self.n * 4 - 1))

    def check_full(self):
        return all(not cell.is_empty() for row in self.board for cell in row)

    def check_winner(self, symbol):
        n = self.n
        # Rows
        for row in self.board:
            if all(cell.value == symbol for cell in row):
                return True
        # Columns
        for col in range(n):
            if all(self.board[row][col].value == symbol for row in range(n)):
                return True
        # Main diagonal
        if all(self.board[i][i].value == symbol for i in range(n)):
            return True
        # Anti-diagonal
        if all(self.board[i][n - 1 - i].value == symbol for i in range(n)):
            return True
        return False

    def play(self):
        is_first_turn = True
        while True:
            player = self.first_player if is_first_turn else self.second_player
            print(f"\n{player.name}'s turn ({player.symbol}). Enter two numbers (0 to {self.n - 1}):")
            try:
                i, j = map(int, input().split())
                if not (0 <= i < self.n and 0 <= j < self.n):
                    print("Invalid coordinates. Try again.")
                    continue
                if not self.board[i][j].is_empty():
                    print(f"Cell ({i}, {j}) is already full. Try another.")
                    continue
            except:
                print("Invalid input. Please enter two integers.")
                continue

            self.board[i][j].set_cell(player.symbol)
            self.display_board()

            if self.check_winner(player.symbol):
                print(f"{player.name} wins the game!")
                break

            if self.check_full():
                print("The game is a draw!")
                break

            is_first_turn = not is_first_turn


if __name__ == '__main__':
    game = Game('Aky', 'X', 'Bky', 'O', 3)
    game.play()

