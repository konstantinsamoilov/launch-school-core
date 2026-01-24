import os
import random

INITIAL_MARKER = ' '
X_MARKER = 'X'
O_MARKER = 'O'
GAMES_TO_WIN_MATCH = 5
WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

def display_board(board, player_marker):
    os.system('clear')

    if player_marker == 'X':
        prompt(f"You are {X_MARKER}. Computer is {O_MARKER}.")
    else:
        prompt(f"Computer is {X_MARKER}. You are {O_MARKER}.")

    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def player_chooses_square(board, player_marker):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()

        if square in valid_choices:
            break

        prompt("Not a valid choice.")

    board[int(square)] = player_marker

def computer_chooses_square(board, player_marker, computer_marker):
    if len(empty_squares(board)) == 0:
        return

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        markers_in_line = [board[sq1], board[sq2], board[sq3]]

        if markers_in_line.count(computer_marker) == 2 and markers_in_line.count(INITIAL_MARKER) == 1:
            if board[sq1] == INITIAL_MARKER:
                square = sq1
            elif board[sq2] == INITIAL_MARKER:
                square = sq2
            else:
                square = sq3
            board[square] = computer_marker
            return
        
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        markers_in_line = [board[sq1], board[sq2], board[sq3]]

        if markers_in_line.count(player_marker) == 2 and markers_in_line.count(INITIAL_MARKER) == 1:
            if board[sq1] == INITIAL_MARKER:
                square = sq1
            elif board[sq2] == INITIAL_MARKER:
                square = sq2
            else:
                square = sq3
            board[square] = computer_marker
            return
        
    if board[5] == ' ':
        board[5] = computer_marker
        return
        
    square = random.choice(empty_squares(board))
    board[square] = computer_marker

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board, player_marker, computer_marker):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if board[sq1] == player_marker and board[sq2] == player_marker and board[sq3] == player_marker:
            return 'Player'
        elif board[sq1] == computer_marker and board[sq2] == computer_marker and board[sq3] == computer_marker:
            return 'Computer'

    return None

def someone_won(board, player_marker, computer_marker):
    return bool(detect_winner(board, player_marker, computer_marker))

def join_or(lst, sepr=', ', last_sepr='or'):
    if lst == []:
        return ""
    elif len(lst) == 1:
        return str(lst[0])
    elif len(lst) == 2:
        return f"{lst[0]} {last_sepr} {lst[1]}"
    else:
        items_to_join = lst[:-1]
        string_items_in_list = []
        
        for item in items_to_join:
            string_items_in_list.append(str(item))
            
        all_but_last_string = sepr.join(string_items_in_list)
        return f"{all_but_last_string}{sepr}{last_sepr} {lst[-1]}"
    
def choose_square(board, current_player, player_marker, computer_marker):
    if current_player == player_marker:
        player_chooses_square(board, player_marker)
    else:
        computer_chooses_square(board, player_marker, computer_marker)

def alternate_player(current_player, player_marker, computer_marker):
    if current_player == player_marker:
        current_player = computer_marker
        return current_player
    else:
        current_player = player_marker
        return current_player

def play_tic_tac_toe(player_marker, computer_marker, current_player):
    player_score = 0
    computer_score = 0
    
    while True:
        board = initialize_board()
        
        while True:
            display_board(board, player_marker)
            choose_square(board, current_player, player_marker, computer_marker)
            current_player = alternate_player(current_player, player_marker, computer_marker)

            if someone_won(board, player_marker, computer_marker) or board_full(board):
                break

        display_board(board, player_marker)

        if someone_won(board, player_marker, computer_marker):
            prompt(f"{detect_winner(board, player_marker, computer_marker)} won!")
        else:
            prompt("It's a tie.")

        if detect_winner(board, player_marker, computer_marker) == 'Player':
            player_score += 1
        elif detect_winner(board, player_marker, computer_marker) == 'Computer':
            computer_score += 1

        prompt(f"Player: {player_score}. Computer: {computer_score}.")

        if player_score == GAMES_TO_WIN_MATCH:
            prompt("Player won 5 games and has won the match! Resetting scores to 0...")
            player_score = 0
            computer_score = 0

        elif computer_score == GAMES_TO_WIN_MATCH:
            prompt("Computer won 5 games and has won the match! Resetting scores to 0...")
            player_score = 0
            computer_score = 0

        prompt("Play again? (Y/y or N/n)")
        answer = input().lower()
        
        while answer != 'n' and answer != 'y':
            prompt("Not a valid choice. Y/y to play again, N/n to exit.")
            answer = input().lower()

        if answer == 'n':
            break
        elif answer == 'y':
            continue

    prompt('Thanks for playing!')

os.system('clear')

prompt(f"(You can play a match, until you or the computer have 5 wins.)")
prompt("Who should go first and have the X markers? " \
        "Type 'Player', 'Computer', or anything else for randomization.")
who_goes_first = input().lower()

if who_goes_first == 'Player'.lower():
    player_marker = 'X'
    computer_marker = 'O'
    current_player = player_marker
elif who_goes_first == 'Computer'.lower():
    player_marker = 'O'
    computer_marker = 'X'
    current_player = computer_marker
else:
    markers = [X_MARKER, O_MARKER]
    random.shuffle(markers)
    player_marker, computer_marker = markers
    current_player = X_MARKER

play_tic_tac_toe(player_marker, computer_marker, current_player)