import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

SHORTCUTS = {
    "r": "rock",
    "p": "paper",
    "sc": "scissors",
    "l": "lizard",
    "sp": "spock"
}

BEATS = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"],
}

def prompt(message):
    print(f"==> {message}")

def determine_winner(player, computer):
    if player == computer:
        return 'tie'
    if computer in BEATS[player]:
        return 'player'
    return 'computer'

def get_player_choice():
    choice = input().strip().lower()

    if choice in SHORTCUTS:
        choice = SHORTCUTS[choice]

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")

        choice = input().strip().lower()

        if choice in SHORTCUTS:
            choice = SHORTCUTS[choice]

    return choice

player_score = 0
computer_score = 0
keep_playing = True

prompt("Hi! This is 'Rock, Paper, Scissors, Lizard, Spock'. "
    "Each fighter beats two others and loses to two others. "
    "First to three wins the match! ")

while keep_playing:

    prompt("Choose your fighter (1-2 chars allowed; "
           "(r)ock, (p)aper, (sc)issors, (l)izard, (sp)ock): ")

    choice = get_player_choice()

    computer_choice = random.choice(VALID_CHOICES)

    result = determine_winner(choice, computer_choice)

    prompt(f"You chose {choice}, computer chose {computer_choice}")

    if result == 'tie':
        prompt("It's a tie!")
    elif result == 'player':
        prompt("You win!")
    else:
        prompt("Computer wins!")

    if result == 'player':
        player_score += 1
    elif result == 'computer':
        computer_score += 1

    prompt(f"Score - You: {player_score}, Computer: {computer_score}")

    if player_score == 3 or computer_score == 3:
        prompt(f"Match winner: {'You' if player_score == 3 else 'Computer'}")
        break

    answer = ''
    while True:
        prompt("Wanna play again (y/n)?")
        answer = input().strip().lower()

        if answer.startswith('y') or answer.startswith('n'):
            break
        prompt("That's not a valid choice.")

    keep_playing = answer.startswith('y')