'''
Minimax algorithm:
There is one new function, minimax, and one rewritten function, computer_chooses_square.

computer_chooses_square is called from choose_square, as the opposite of player_chooses_square.

1. Initialize best_score to point to -11, lower than our absolute minimum for minimax.
    best_score points to the value of the best of the outcomes of the computer choosing a particular square as the next square.

2. Initialize best_move to None, at the start.
    computer_chooses_square sees the current state of the board.

3. For each square of the squares that are still empty,
    1. create a temporary board and point it to the copy of the current board,
    2. mark that square on the temporary board with the computer marker,
    3. and call `minimax`, passing it the temporary board and a 'False' boolean, signifying that the next turn is the player's.

4. minimax runs. Immediately it calls detect_winner and board_full with the temporary board.
    Those two functions check if there are winning lines or no more moves to be made. if not, then:

5. If it's the computer's turn (boolean would be True), 
    best_outcome points to -11. This is the outcome of perfect continuation of play from that one square...

5.5. But it is also the best outcome for each particular tree, and each move (depending on where minimax is).

"The deepest call (let's say Level 9) is on a full board. It's a tie. It hits a base case and returns 0.
Where does it return to? To the paused Level 8 function that called it.

Level 8 receives the 0 into its score variable. It uses this 0 in its min() or max() calculation.
It finishes its own loop (by exploring other potential moves from its state) and calculates its own best_outcome.

Then, Level 8 returns its calculated best_outcome.
Where does it return to? To the paused Level 7 function that called it.
Level 7 receives the value from Level 8, uses it in its own calculation,
finishes its loop, and returns its own result to Level 6."

6.      For each empty square in the temporary board that minimax got,
            create a 'minimax_temp_board' by copying temp_board
            (so basically a clone of temp_board, every time).
            Then, mark that square on minimax_temp_board with the computer marker.

            Then, init 'score' and point it to the recursive call of minimax, passing it minimax_temp_board and boolean False (so player would move next).
            That will return -10, 0 or 10 (as best_outcome), which `score` will point to.

            Then point best_outcome once more, to the maximum of best_outcome and score.
            As recursive minimax is called for different minimax_temp_boards, best_outcome will be updated.

            For the player, the logic is the same, except best_outcome will be selected from the MINIMUM of best_outcome and score.

7. Once minimax finishes running for the initial square that computer_chooses_square passed it,
    'return best_outcome' returns into 'move_score = minimax(temp_board, False, player_marker, computer_marker)'
    and becomes 'move_score'

8. If that move_score is higher than the best_score so far, best_score is updated to it,
    and the current square being assessed is also now what best_move will point to.

9. After all the squares are assessed, if there is a best_move (there will be one),
    the best_move (an integer) on the real board will refer to 'computer_marker', and so the board will be marked.

P.S. When playing via this, the computer will always choose the same square for any particular position, because
either that's the single best square to move to next, or it's the first evaluated one among 'equals', and so
best_move doesn't get updated afterwards. And it doesn't select the 5 square by default.
'''

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

def minimax(temp_board, computer_next, player_marker, computer_marker):
    if detect_winner(temp_board, player_marker, computer_marker) == 'Computer':
        return 10
    elif detect_winner(temp_board, player_marker, computer_marker) == 'Player':
        return -10
    elif board_full(temp_board):
        return 0
    
    if computer_next:
        best_outcome = -11

        for square in empty_squares(temp_board):
            minimax_temp_board = temp_board.copy()
            minimax_temp_board[int(square)] = computer_marker
            score = minimax(minimax_temp_board, False, player_marker, computer_marker)
            best_outcome = max(best_outcome, score)

        return best_outcome
    
    else:
        best_outcome = 11

        for square in empty_squares(temp_board):
            minimax_temp_board = temp_board.copy()
            minimax_temp_board[int(square)] = player_marker
            score = minimax(minimax_temp_board, True, player_marker, computer_marker)
            best_outcome = min(best_outcome, score)

        return best_outcome

def computer_chooses_square(board, player_marker, computer_marker):
    best_score = -11
    best_move = None

    for square in empty_squares(board):
        temp_board = board.copy()
        temp_board[square] = computer_marker

        move_score = minimax(temp_board, computer_next=False, player_marker=player_marker, computer_marker=computer_marker)

        if move_score > best_score:
            best_score = move_score
            best_move = square

    if best_move:
        board[best_move] = computer_marker

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board, player_marker, computer_marker):
    return bool(detect_winner(board, player_marker, computer_marker))

def detect_winner(board, player_marker, computer_marker):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if board[sq1] == player_marker and board[sq2] == player_marker and board[sq3] == player_marker:
            return 'Player'
        elif board[sq1] == computer_marker and board[sq2] == computer_marker and board[sq3] == computer_marker:
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

def play_tic_tac_toe():
    prompt(f"(You can play a match, until you or the computer have 5 wins.)")
    player_score = 0
    computer_score = 0

    while True:
        prompt("Who should go first and have the X markers? " \
                "Type 'Player', 'Computer', or anything else to randomize.")
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

play_tic_tac_toe()