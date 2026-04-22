import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    X_MARKER = "X"
    O_MARKER = "O"
    I_MARKER = "I"

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
        self.squares = {key: Square() for key in range(1, 26)}

    def display(self):
        print('')
        print('1    |2    |3    |4    |5 ')
        print(f"  {self.squares[1]}  |  {self.squares[2]}  |  {self.squares[3]}  |  {self.squares[4]}  |  {self.squares[5]}")
        print('     |     |     |     |')
        print('-----+-----+-----+-----+-----')
        print('6    |7    |8    |9    |10 ')
        print(f"  {self.squares[6]}  |  {self.squares[7]}  |  {self.squares[8]}  |  {self.squares[9]}  |  {self.squares[10]}")
        print('     |     |     |     |')
        print('-----+-----+-----+-----+-----')
        print('11   |12   |13   |14   |15 ')
        print(f"  {self.squares[11]}  |  {self.squares[12]}  |  {self.squares[13]}  |  {self.squares[14]}  |  {self.squares[15]}")
        print('     |     |     |     |')
        print('-----+-----+-----+-----+-----')
        print('16   |17   |18   |19   |20 ')
        print(f"  {self.squares[16]}  |  {self.squares[17]}  |  {self.squares[18]}  |  {self.squares[19]}  |  {self.squares[20]}")
        print('     |     |     |     |')
        print('-----+-----+-----+-----+-----')
        print('21   |22   |23   |24   |25 ')
        print(f"  {self.squares[21]}  |  {self.squares[22]}  |  {self.squares[23]}  |  {self.squares[24]}  |  {self.squares[25]}")
        print('     |     |     |     |')
        print('')

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
        self.squares = {key: Square() for key in range(1, 26)}

    def second_tier_initial_markers(self):
        second_tier_available = []
        for sq in TTTGame.SECOND_TIER:
            if self.squares[sq].is_unused():
                second_tier_available.append(sq)
        return second_tier_available

    def third_tier_initial_markers(self):
        third_tier_available = []
        for sq in TTTGame.THIRD_TIER:
            if self.squares[sq].is_unused():
                third_tier_available.append(sq)
        return third_tier_available

class Player:
    def __init__(self, marker, name):
        self.marker = marker
        self.name = name
        self.score = 0

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

    def move(self, game):
        raise NotImplementedError("Each subclass must implement its own move method.")

class Human(Player):
    def __init__(self, marker):
        super().__init__(marker, "You")

    def move(self, game):
        valid_choices = game.board.unused_squares()
        choices_list = [str(choice) for choice in valid_choices]

        for p in game.players:
            print(f'{p.name}: {p.marker} marker.')

        while True:
            choice = input(f"Choose a square ({TTTGame._join_or(choices_list)}): ")
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, not a valid choice.")
            print()

        game.board.mark_square_at(choice, self.marker)

class Computer(Player):
    def __init__(self, marker, name):
        super().__init__(marker, name)

    def move(self, game):
        offensive_move = game.find_critical_square(self)
        if offensive_move:
            game.board.mark_square_at(offensive_move, self.marker)
            return

        opponents = game.get_opponents(self)
        for opponent in opponents:
            defensive_move = game.find_critical_square(opponent)
            if defensive_move:
                game.board.mark_square_at(defensive_move, self.marker)
                return

        second_tier_options = game.board.second_tier_initial_markers()
        third_tier_options = game.board.third_tier_initial_markers()

        if game.board.squares[TTTGame.CENTER_SQUARE].is_unused():
            choice = TTTGame.CENTER_SQUARE
        elif second_tier_options:
            choice = random.choice(second_tier_options)
        elif third_tier_options:
            choice = random.choice(third_tier_options)
        else:
            choice = random.choice(game.board.unused_squares())

        game.board.mark_square_at(choice, self.marker)

class TTTGame:
    MATCH_GOAL = 3
    MARKERS_IN_ROW = 4
    POSSIBLE_WINNING_ROWS = [
            [1, 2, 3, 4], [2, 3, 4, 5], [6, 7, 8, 9],
            [7, 8, 9, 10], [11, 12, 13, 14], [12, 13, 14, 15],
            [16, 17, 18, 19], [17, 18, 19, 20], [21, 22, 23, 24],
            [22, 23, 24, 25], [1, 6, 11, 16], [6, 11, 16, 21],
            [2, 7, 12, 17], [7, 12, 17, 22], [3, 8, 13, 18],
            [8, 13, 18, 23], [4, 9, 14, 19], [9, 14, 19, 24],
            [5, 10, 15, 20], [10, 15, 20, 25], [1, 7, 13, 19],
            [7, 13, 19, 25], [5, 9, 13, 17], [9, 13, 17, 21]
        ]
    CENTER_SQUARE = 13
    SECOND_TIER = [7, 8, 9, 12, 14, 17, 18, 19]
    THIRD_TIER = [2, 4, 6, 10, 16, 20, 22, 24]
    FOURTH_TIER = [1, 3, 5, 11, 15, 21, 23, 25]

    def __init__(self):
        self.board = Board()

        markers = [Square.X_MARKER,
                   Square.O_MARKER,
                   Square.I_MARKER]
        random.shuffle(markers)

        self.human = Human(markers.pop())
        self.amadou = Computer(markers.pop(), "Amadou")
        self.mariam = Computer(markers.pop(), "Mariam")

        self.players = [self.human, self.amadou, self.mariam]

        self.marker_order = {Square.X_MARKER: 0, Square.O_MARKER: 1, Square.I_MARKER: 2}

        self.players.sort(key=self.get_sort_key)

        self.current_player_idx = 0

    def play_once(self):
        self.board.display()

        while True:
            current_player = self.players[self.current_player_idx]
            current_player.move(self)

            if self.is_game_over():
                self.board.display_with_clear()
                break

            self.board.display_with_clear()
            self.next_player()

        self.display_results()
        self.update_score()
        self.display_score()

    def play_again(self):
        while True:
            again = input("Want to play again? (y/n): ").lower()
            if again == 'y':
                self.board.reset()
                return True
            if again == 'n':
                return False
            print("Invalid input.")

    def find_critical_square(self, player):
        for row in self.POSSIBLE_WINNING_ROWS:
            if self.board.count_markers_for(player, row) == 3:
                for key in row:
                    if self.board.squares[key].is_unused():
                        return key
        return None

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to TTT!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing!")

    def display_results(self):
        for p in self.players:
            if self.is_winner(p):
                print(f"{p.name} won!")
                return
            
        print("It's a tie.")

    def display_score(self):
        print(f'Human: {self.human.score}. Amadou: {self.amadou.score}. Mariam: {self.mariam.score}.')

    def match_over(self):
        for p in self.players:
            if p.score == self.MATCH_GOAL:
                print(f"{p.name} won the match!")
                return True
        return False

    def four_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == self.MARKERS_IN_ROW

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.four_in_a_row(player, row):
                return True
        return False

    def someone_won(self):
        return any(self.is_winner(p) for p in self.players)

    def update_score(self):
        for player in self.players:
            if self.is_winner(player):
                player.score += 1
                break

    def get_sort_key(self, player):
        return self.marker_order[player.marker]
    
    def next_player(self):
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

    def get_opponents(self, current_player):
        return [p for p in self.players if p != current_player]

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

game.display_goodbye_message()