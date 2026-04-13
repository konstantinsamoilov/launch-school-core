import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')

    def __init__(self):
        self.move = None

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        while True:
            choice = input("Choose rock, paper, scissors, lizard or spock: ").lower()
            if choice in Player.CHOICES:
                break

            print(f'{choice} is not valid.')

        self.move = choice

class Computer_Normal(Player):
    def __init__(self):
        super().__init__()

    def choose(self, human_move):
        self.move = random.choice(Player.CHOICES)

class Computer_Fever_Ray(Player):
    def __init__(self):
        super().__init__()
        self.previous_human_move = None

    def choose(self, human_move):
        if RPSGame._move_counter == 0:
            self.move = random.choice(Player.CHOICES)
        else:
            self.move = self.previous_human_move

        self.previous_human_move = human_move

class Computer_Melody(Player):
    def __init__(self):
        super().__init__()

    def choose(self, human_move):
        self.weights = [1, 3, 1, 1, 1]
        self.move = random.choices(Player.CHOICES, weights=self.weights, k=1)[0]

class Computer_KKB(Player):
    def __init__(self):
        super().__init__()

    def choose(self, human_move):
        self.move = 'lizard'

class RPSGame:
    OPPONENT_CHOICES = {
        'normal': Computer_Normal,
        'fever ray': Computer_Fever_Ray,
        'melody': Computer_Melody,
        'kkb': Computer_KKB,
    }

    _move_counter = 0

    def __init__(self):
        self._human = Human()
        self._human_score = 0
        self._computer_score = 0
        self._history_dict = {}

    def _display_welcome_message(self):
        print('Welcome to RPS!')

    def _opponent_choice(self):
        while True:
            opponent_choice = input("Choose your opponent: normal, fever ray, melody or kkb: ").lower()
            if opponent_choice in self.OPPONENT_CHOICES:
                break

            print(f'{opponent_choice} is not valid.')

        self._computer = self.OPPONENT_CHOICES[opponent_choice]()
        print(f"Your opponent is {opponent_choice}.")

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move in ['lizard', 'scissors']) or
            (human_move == 'paper' and computer_move in ['rock', 'spock']) or
            (human_move == 'scissors' and computer_move in ['lizard', 'paper']) or
            (human_move == 'lizard' and computer_move in ['paper', 'spock']) or
            (human_move == 'spock' and computer_move in ['rock', 'scissors']))

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move in ['lizard', 'scissors']) or
            (computer_move == 'paper' and human_move in ['rock', 'spock']) or
            (computer_move == 'scissors' and human_move in ['lizard', 'paper']) or
            (computer_move == 'lizard' and human_move in ['paper', 'spock']) or
            (computer_move == 'spock' and human_move in ['rock', 'scissors']))

    def _score(self):
        if self._human_wins():
            self._human_score += 1
        elif self._computer_wins():
            self._computer_score += 1

        if self._human_score == 5:
            print(f"Human won 5 times and has won the match!")
            print("Resetting scores to 0...")
            self._human_score = 0
            self._computer_score = 0

        elif self._computer_score == 5:
            print(f"Computer won 5 times and has won the match!")
            print("Resetting scores to 0...")
            self._human_score = 0
            self._computer_score = 0

    def _display_winner(self):
        print('')
        print(f'You chose: {self._human.move}')
        print(f'Computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win!')
            print('')
        elif self._computer_wins():
            print('Computer wins!')
            print('')
        else:
            print("It's a tie.")
            print('')

        print(f"Human: {self._human_score} win(s). Computer: {self._computer_score} win(s).")
        print('')
        print(f"Move history: ")
        print(self._history_dict)

    def _move_history(self):
        RPSGame._move_counter += 1
        self._history_dict[f'Move {self._move_counter}'] = f'Human: {self._human.move}, Computer: {self._computer.move}'

    def _play_again(self):
        answer = input("Do you want to play again? (y/n) ")
        return answer.lower().startswith('y')

    def _display_goodbye_message(self):
        print('Thanks for playing!')

    def play(self):
        self._display_welcome_message()
        self._opponent_choice()

        while True:
            self._human.choose()
            self._computer.choose(self._human.move)
            self._score()
            self._move_history()
            self._display_winner()

            if not self._play_again():
                break

        self._display_goodbye_message()

RPSGame().play()