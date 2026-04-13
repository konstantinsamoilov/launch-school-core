import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |  {self.squares[2]}  |  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |  {self.squares[5]}  |  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |  {self.squares[8]}  |  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def reset(self):
        self.squares = {key: Square() for key in range(1, 10)}

class Player:
    def __init__(self, marker):
        self.marker = marker
        self.score = 0

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    MATCH_GOAL = 3

    MARKERS_IN_ROW = 3

    POSSIBLE_WINNING_ROWS = (
    (1, 2, 3),  # top row of board
    (4, 5, 6),  # center row of board
    (7, 8, 9),  # bottom row of board
    (1, 4, 7),  # left column of board
    (2, 5, 8),  # middle column of board
    (3, 6, 9),  # right column of board
    (1, 5, 9),  # diagonal: top-left to bottom-right
    (3, 5, 7),  # diagonal: top-right to bottom-left
)

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.first_player = self.human

    def play_once(self):
        current_player = self.first_player

        self.board.display()

        while True:
            self.player_moves(current_player)
            if self.is_game_over():
                self.board.display_with_clear()
                break

            self.board.display_with_clear()
            current_player = self.toggle_player(current_player)

        self.display_results()
        self.update_score()
        self.display_score()

    def toggle_player(self, player):
        return self.computer if player == self.human else self.human

    def player_moves(self, current_player):
        if current_player == self.human:
            self.human_moves()
        else:
            self.computer_moves()

    def play_again(self):
        while True:
            again = input("Want to play again? (y/n): ").lower()
            if again == 'y':
                self.board.reset()
                return True
            if again == 'n':
                return False
            print("Invalid input.")

    def human_moves(self):
        valid_choices = self.board.unused_squares()
        choices_list = [str(choice) for choice in valid_choices]

        while True:
            choice = input(f"Choose a square ({self._join_or(choices_list)}): ")
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def _find_critical_square(self, player):
        for row in self.POSSIBLE_WINNING_ROWS:
            if self.board.count_markers_for(player, row) == 2:
                for key in row:
                    if self.board.squares[key].is_unused():
                        return key
        return None

    def computer_moves(self):
        choice = self._find_critical_square(self.computer) # offensive

        if not choice:
            choice = self._find_critical_square(self.human) # defensive

        if not choice:
            if self.board.squares[5].is_unused():
                choice = 5
            else:
                choice = random.choice(self.board.unused_squares())

        self.board.mark_square_at(choice, self.computer.marker)

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to TTT!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing!")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won!")
        elif self.is_winner(self.computer):
            print("Computer won!")
        else:
            print("A tie.")

    def display_score(self):
        print(f'Human: {self.human.score}. Computer: {self.computer.score}')

    def match_over(self):
        if self.human.score == self.MATCH_GOAL:
            print("You have won the match!")
            return True
        
        if self.computer.score == self.MATCH_GOAL:
            print("Computer has won the match!")
            return True
        
        return False

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == self.MARKERS_IN_ROW

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True
        return False

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

    def update_score(self):
        if self.is_winner(self.human):
            self.human.score += 1
        elif self.is_winner(self.computer):
            self.computer.score += 1

    @staticmethod
    def _join_or(choices_list, first_sep=', ', second_sep='or '):
        if len(choices_list) > 2:
            choices_str = first_sep.join(choices_list[0:-1])
            return choices_str + first_sep + second_sep + str(choices_list[-1])
        
        if len(choices_list) == 2:
            return str(choices_list[0]) + ' ' + second_sep + str(choices_list[-1])
        
        return choices_list[0]

game = TTTGame()
game.display_welcome_message()

while True:
    game.play_once()

    if game.match_over():
        break

    if not game.play_again():
        break

    game.first_player = game.toggle_player(game.first_player)

game.display_goodbye_message()