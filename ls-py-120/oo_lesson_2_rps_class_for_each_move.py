import random

class Move:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self._value
    
class Rock(Move):
    def __init__(self):
        super().__init__('rock')

    def __gt__(self, other_move):
        return other_move._value in ['scissors', 'lizard']
    
class Paper(Move):
    def __init__(self):
        super().__init__('paper')

    def __gt__(self, other_move):
        return other_move._value in ['rock', 'spock']
    
class Scissors(Move):
    def __init__(self):
        super().__init__('scissors')

    def __gt__(self, other_move):
        return other_move._value in ['paper', 'lizard']
    
class Lizard(Move):
    def __init__(self):
        super().__init__('lizard')

    def __gt__(self, other_move):
        return other_move._value in ['paper', 'spock']
    
class Spock(Move):
    def __init__(self):
        super().__init__('spock')

    def __gt__(self, other_move):
        return other_move._value in ['rock', 'scissors']
    
class Player:
    MOVE_CLASSES = {
        'rock': Rock,
        'paper': Paper,
        'scissors': Scissors,
        'lizard': Lizard,
        'spock': Spock,
    }

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

        self.move = Player.MOVE_CLASSES[choice]()

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(list(Player.MOVE_CLASSES.values()))()

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._human_score = 0
        self._computer_score = 0

    def _display_welcome_message(self):
        print('Welcome to RPS!')

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return human_move > computer_move

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return computer_move > human_move

    def _display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win!')
        elif self._computer_wins():
            print('Computer wins!')
        else:
            print("It's a tie.")

        print(f"Human: {self._human_score} win(s). Computer: {self._computer_score} win(s).")

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

    def _play_again(self):
        answer = input("Do you want to play again? (y/n) ")
        return answer.lower().startswith('y')

    def _display_goodbye_message(self):
        print('Thanks for playing!')

    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            self._score()
            self._display_winner()

            if not self._play_again():
                break

        self._display_goodbye_message()

RPSGame().play()