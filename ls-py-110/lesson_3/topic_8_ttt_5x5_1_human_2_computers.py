'''
Tic-Tac-Toe (5x5 with two computers and one human):
1. We're not using minimax because, with a 5x5 board, there are way too many paths to calculate;
    the program tries, but it would take way too long.

2. I put numbers of squares on the board for the user to see at all times.

3. I don't know what the fairest rules for a 3-player 5x5 TTT would be, so I set it as '4-in-a-row'.
    There are 24 winning lines, which is many. It's like a slot machine...

4. In 3-player 5x5, there are four tiers of squares. 
    Middle, 13, is by far the best. (8 winning lines)
    Then the squares around it. (6 winning lines)
    Then the squares at edges where you can still make a diagonal. (4 winning lines)
    Then the squares that either can't make a diagonal, or can't be part of two lines on their row/column. (3 winning lines)

5. Because (I assume) the advantage of going earlier is very strong in a 3-player game, the player no longer has an option to
    choose their markers. It's random every time.

6. 'who_is_who' prints players in order of X-O-I specifically.

7. 'computer_chooses_square' has basically the same code twice for the two AIs. Could be consolidated.

8. 'alternate_player' now flips between the three types of markers.

9. 'play_tic_tac_toe' now does not take any arguments, and scores and shuffling of markers is now done
    inside the function. Also updating the other versions of tic-tac-toe to do this.

10. The AIs are named after Amadou & Mariam, a pop duo from Mali. <3
'''

import random

INITIAL_MARKER = ' '
X_MARKER = 'X'
O_MARKER = 'O'
I_MARKER = 'I'
GAMES_TO_WIN_MATCH = 5
SECOND_TIER = [7, 8, 9, 12, 14, 17, 18, 19]
THIRD_TIER = [2, 4, 6, 10, 16, 20, 22, 24]
FOURTH_TIER = [1, 3, 5, 11, 15, 21, 23, 25]
WINNING_LINES = [
        [1, 2, 3, 4], [2, 3, 4, 5], [6, 7, 8, 9],
        [7, 8, 9, 10], [11, 12, 13, 14], [12, 13, 14, 15],
        [16, 17, 18, 19], [17, 18, 19, 20], [21, 22, 23, 24],
        [22, 23, 24, 25], [1, 6, 11, 16], [6, 11, 16, 21],
        [2, 7, 12, 17], [7, 12, 17, 22], [3, 8, 13, 18],
        [8, 13, 18, 23], [4, 9, 14, 19], [9, 14, 19, 24],
        [5, 10, 15, 20], [10, 15, 20, 25], [1, 7, 13, 19],
        [7, 13, 19, 25], [5, 9, 13, 17], [9, 13, 17, 21]
    ]

def who_is_who(player_marker, amadou_marker, mariam_marker, current_player, second_player, third_player):
    if current_player == player_marker:
        prompt(f"You are {X_MARKER}.")
    elif current_player == amadou_marker:
        prompt(f"Amadou is {X_MARKER}.")
    elif current_player == mariam_marker:
        prompt(f"Mariam is {X_MARKER}.")

    if second_player == player_marker:
        prompt(f"You are {O_MARKER}.")
    elif second_player == amadou_marker:
        prompt(f"Amadou is {O_MARKER}.")
    elif second_player == mariam_marker:
        prompt(f"Mariam is {O_MARKER}.")

    if third_player == player_marker:
        prompt(f"You are {I_MARKER}.")
    elif third_player == amadou_marker:
        prompt(f"Amadou is {I_MARKER}.")
    elif third_player == mariam_marker:
        prompt(f"Mariam is {I_MARKER}.")

def display_board(board):
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
        prompt(f'Choose a square ({join_or(valid_choices)}):')
        square = input().strip()

        if square in valid_choices:
            break

        prompt("Not a valid choice.")

    board[int(square)] = player_marker

def computer_chooses_square(board, player_marker, amadou_marker, mariam_marker, current_player):
    if current_player == amadou_marker:

        if len(empty_squares(board)) == 0:
            return

        for line in WINNING_LINES:
            sq1, sq2, sq3, sq4 = line
            markers_in_line = [board[sq] for sq in line]

            if markers_in_line.count(amadou_marker) == 3 and markers_in_line.count(INITIAL_MARKER) == 1:
                initial_marker_sq_idx = markers_in_line.index(INITIAL_MARKER)
                marker_goes_here = line[initial_marker_sq_idx]
                prompt(f'Amadou selects square {marker_goes_here}.')
                board[marker_goes_here] = amadou_marker
                return
            
        for line in WINNING_LINES:
            sq1, sq2, sq3, sq4 = line
            markers_in_line = [board[sq] for sq in line]

            if markers_in_line.count(player_marker) == 3 and markers_in_line.count(INITIAL_MARKER) == 1:
                initial_marker_sq_idx = markers_in_line.index(INITIAL_MARKER)
                marker_goes_here = line[initial_marker_sq_idx]
                prompt(f'Amadou selects square {marker_goes_here}.')
                board[marker_goes_here] = amadou_marker
                return
            
        if board[13] == ' ':
            prompt(f'Amadou selects square 13.')
            board[13] = amadou_marker
            return

        second_tier_initial_markers = []
        for sq in SECOND_TIER:
            if board[sq] == INITIAL_MARKER:
                second_tier_initial_markers.append(sq)

        if second_tier_initial_markers:
            second_tier_random_square = random.choice(second_tier_initial_markers)
            prompt(f'Amadou selects square {second_tier_random_square}.')
            board[second_tier_random_square] = amadou_marker
            return

        third_tier_initial_markers = []
        for sq in THIRD_TIER:
            if board[sq] == INITIAL_MARKER:
                third_tier_initial_markers.append(sq)

        if third_tier_initial_markers:
            third_tier_random_square = random.choice(third_tier_initial_markers)
            prompt(f'Amadou selects square {third_tier_random_square}.')
            board[third_tier_random_square] = amadou_marker
            return
        
        fourth_tier_initial_markers = []
        for sq in FOURTH_TIER:
            if board[sq] == INITIAL_MARKER:
                fourth_tier_initial_markers.append(sq)

        if fourth_tier_initial_markers:
            fourth_tier_random_square = random.choice(fourth_tier_initial_markers)
            prompt(f'Amadou selects square {fourth_tier_random_square}.')
            board[fourth_tier_random_square] = amadou_marker
            return

    elif current_player == mariam_marker:

        if len(empty_squares(board)) == 0:
            return

        for line in WINNING_LINES:
            sq1, sq2, sq3, sq4 = line
            markers_in_line = [board[sq] for sq in line]

            if markers_in_line.count(mariam_marker) == 3 and markers_in_line.count(INITIAL_MARKER) == 1:
                initial_marker_sq_idx = markers_in_line.index(INITIAL_MARKER)
                marker_goes_here = line[initial_marker_sq_idx]
                prompt(f'Mariam selects square {marker_goes_here}.')
                board[marker_goes_here] = mariam_marker
                return
            
        for line in WINNING_LINES:
            sq1, sq2, sq3, sq4 = line
            markers_in_line = [board[sq] for sq in line]

            if markers_in_line.count(player_marker) == 3 and markers_in_line.count(INITIAL_MARKER) == 1:
                initial_marker_sq_idx = markers_in_line.index(INITIAL_MARKER)
                marker_goes_here = line[initial_marker_sq_idx]
                prompt(f'Mariam selects square {marker_goes_here}.')
                board[marker_goes_here] = mariam_marker
                return
            
        if board[13] == ' ':
            prompt(f'Mariam selects square 13.')
            board[13] = mariam_marker
            return

        second_tier_initial_markers = []
        for sq in SECOND_TIER:
            if board[sq] == INITIAL_MARKER:
                second_tier_initial_markers.append(sq)

        if second_tier_initial_markers:
            second_tier_random_square = random.choice(second_tier_initial_markers)
            prompt(f'Mariam selects square {second_tier_random_square}.')
            board[second_tier_random_square] = mariam_marker
            return

        third_tier_initial_markers = []
        for sq in THIRD_TIER:
            if board[sq] == INITIAL_MARKER:
                third_tier_initial_markers.append(sq)

        if third_tier_initial_markers:
            third_tier_random_square = random.choice(third_tier_initial_markers)
            prompt(f'Mariam selects square {third_tier_random_square}.')
            board[third_tier_random_square] = mariam_marker
            return
        
        fourth_tier_initial_markers = []
        for sq in FOURTH_TIER:
            if board[sq] == INITIAL_MARKER:
                fourth_tier_initial_markers.append(sq)

        if fourth_tier_initial_markers:
            fourth_tier_random_square = random.choice(fourth_tier_initial_markers)
            prompt(f'Mariam selects square {fourth_tier_random_square}.')
            board[fourth_tier_random_square] = mariam_marker
            return
    
def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board, player_marker, amadou_marker, mariam_marker):
    return bool(detect_winner(board, player_marker, amadou_marker, mariam_marker))

def detect_winner(board, player_marker, amadou_marker, mariam_marker):
    for line in WINNING_LINES:
        markers_in_line = [board[sq] for sq in line]

        if markers_in_line.count(player_marker) == 4:
            return 'Player'
        elif markers_in_line.count(amadou_marker) == 4:
            return 'Amadou'
        elif markers_in_line.count(mariam_marker) == 4:
            return 'Mariam'

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
    
def choose_square(board, player_marker, amadou_marker, mariam_marker, current_player):
    if current_player == player_marker:
        player_chooses_square(board, player_marker)
    else:
        computer_chooses_square(board, player_marker, amadou_marker, mariam_marker, current_player)

def alternate_player(current_player):
    if current_player == X_MARKER:
        current_player = O_MARKER
        return current_player

    elif current_player == O_MARKER:
        current_player = I_MARKER
        return current_player

    elif current_player == I_MARKER:
        current_player = X_MARKER
        return current_player
    
def play_tic_tac_toe():
    prompt(f"(You can play a match, until you or either computer (Amadou or Mariam) have 5 wins.)")
    player_score = 0
    amadou_score = 0
    mariam_score = 0

    while True:
        board = initialize_board()
        markers = [X_MARKER, O_MARKER, I_MARKER]
        random.shuffle(markers)
        player_marker, amadou_marker, mariam_marker = markers
        current_player = X_MARKER
        second_player = O_MARKER
        third_player = I_MARKER
        who_is_who(player_marker, amadou_marker, mariam_marker, current_player, second_player, third_player)
        
        while True:
            display_board(board)
            choose_square(board, player_marker, amadou_marker, mariam_marker, current_player)
            current_player = alternate_player(current_player)

            if someone_won(board, player_marker, amadou_marker, mariam_marker) or board_full(board):
                break

        display_board(board)

        if someone_won(board, player_marker, amadou_marker, mariam_marker):
            prompt(f"{detect_winner(board, player_marker, amadou_marker, mariam_marker)} won!")
        else:
            prompt("It's a tie.")

        if detect_winner(board, player_marker, amadou_marker, mariam_marker) == 'Player':
            player_score += 1
        elif detect_winner(board, player_marker, amadou_marker, mariam_marker) == 'Amadou':
            amadou_score += 1
        elif detect_winner(board, player_marker, amadou_marker, mariam_marker) == 'Mariam':
            mariam_score += 1

        prompt(f"Player: {player_score}. Amadou: {amadou_score}. Mariam: {mariam_score}.")

        if player_score == GAMES_TO_WIN_MATCH:
            prompt("You won 5 games and have won the match! Resetting scores to 0...")
            player_score = 0
            amadou_score = 0
            mariam_score = 0

        elif amadou_score == GAMES_TO_WIN_MATCH:
            prompt("Amadou won 5 games and has won the match! Resetting scores to 0...")
            player_score = 0
            amadou_score = 0
            mariam_score = 0

        elif mariam_score == GAMES_TO_WIN_MATCH:
            prompt("Mariam won 5 games and has won the match! Resetting scores to 0...")
            player_score = 0
            amadou_score = 0
            mariam_score = 0

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

play_tic_tac_toe()