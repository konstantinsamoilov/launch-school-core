'''
1. We're not using minimax because, with a 5x5 board, there are way too many paths to calculate; the program tries, but it would take way too long.

2. I put numbers of squares on the board for the user to see at all times.

3. We're keeping the order of AI offense - AI defense - center square (13 here) and adding two more tiers:
    second tier, with eight numbers that are part of three types of lines (row, column, diagonal);
    third tier, the rest of the numbers, that are part of two types of lines (row and column)

    We create constants for squares in those two tiers.
    Then, in the function, we init a 'second_tier_initial_markers' empty list,
        and for square in SECOND_TIER,
            if that square on the board is an INITIAL_MARKER,
                we append it to the list.

    Then if it's not empty,
        we choose randomly between the squares,
            and computer_marks that picked square.

    Same for third tier.
'''

import os
import random
from copy import copy

INITIAL_MARKER = ' '
X_MARKER = 'X'
O_MARKER = 'O'
GAMES_TO_WIN_MATCH = 5
SECOND_TIER = [1, 5, 7, 9, 17, 19, 21, 25]
THIRD_TIER = [2, 3, 4, 6, 8, 10, 11, 12, 14, 15, 16, 18, 20, 22, 23, 24]
WINNING_LINES = [
        [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [1, 6, 11, 16, 21],
        [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24],
        [5, 10, 15, 20, 25], [1, 7, 13, 19, 25], [5, 9, 13, 17, 21]
    ]

def display_board(board, player_marker):
    os.system('clear')

    if player_marker == 'X':
        prompt(f"You are {X_MARKER}. Computer is {O_MARKER}.")
    else:
        prompt(f"Computer is {X_MARKER}. You are {O_MARKER}.")

    print('')
    print('1    |2    |3    |4    |5 ')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  |  {board[4]}  |  {board[5]}")
    print('     |     |     |     |')
    print('-----+-----+-----+-----+-----')
    print('6    |7    |8    |9    |10 ')
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  |  {board[9]}  |  {board[10]}")
    print('     |     |     |     |')
    print('-----+-----+-----+-----+-----')
    print('11   |12   |13   |14   |15 ')
    print(f"  {board[11]}  |  {board[12]}  |  {board[13]}  |  {board[14]}  |  {board[15]}")
    print('     |     |     |     |')
    print('-----+-----+-----+-----+-----')
    print('16   |17   |18   |19   |20 ')
    print(f"  {board[16]}  |  {board[17]}  |  {board[18]}  |  {board[19]}  |  {board[20]}")
    print('     |     |     |     |')
    print('-----+-----+-----+-----+-----')
    print('21   |22   |23   |24   |25 ')
    print(f"  {board[21]}  |  {board[22]}  |  {board[23]}  |  {board[24]}  |  {board[25]}")
    print('     |     |     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 26)}

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
        sq1, sq2, sq3, sq4, sq5 = line
        markers_in_line = [board[sq] for sq in line]

        if markers_in_line.count(computer_marker) == 4 and markers_in_line.count(INITIAL_MARKER) == 1:
            initial_marker_sq_idx = markers_in_line.index(INITIAL_MARKER)
            marker_goes_here = line[initial_marker_sq_idx]
            print(marker_goes_here)
            board[marker_goes_here] = computer_marker
            return
        
    for line in WINNING_LINES:
        sq1, sq2, sq3, sq4, sq5 = line
        markers_in_line = [board[sq] for sq in line]

        if markers_in_line.count(player_marker) == 4 and markers_in_line.count(INITIAL_MARKER) == 1:
            initial_marker_sq_idx = markers_in_line.index(INITIAL_MARKER)
            marker_goes_here = line[initial_marker_sq_idx]
            print(marker_goes_here)
            board[marker_goes_here] = computer_marker
            return
        
    if board[13] == ' ':
        board[13] = computer_marker
        return

    second_tier_initial_markers = []
    for sq in SECOND_TIER:
         if board[sq] == INITIAL_MARKER:
             second_tier_initial_markers.append(sq)

    if second_tier_initial_markers:
        second_tier_random_square = random.choice(second_tier_initial_markers)
        board[second_tier_random_square] = computer_marker
        return

    third_tier_initial_markers = []
    for sq in THIRD_TIER:
        if board[sq] == INITIAL_MARKER:
            third_tier_initial_markers.append(sq)

    if third_tier_initial_markers:
        third_tier_random_square = random.choice(third_tier_initial_markers)
        board[third_tier_random_square] = computer_marker
        return
    
def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board, player_marker, computer_marker):
    return bool(detect_winner(board, player_marker, computer_marker))

def detect_winner(board, player_marker, computer_marker):
    for line in WINNING_LINES:
        markers_in_line = [board[sq] for sq in line]

        if markers_in_line.count(player_marker) == 5:
            return 'Player'
        elif markers_in_line.count(computer_marker) == 5:
            return 'Computer'

    return None

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