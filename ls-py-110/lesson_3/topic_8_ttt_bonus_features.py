# 1 (Improved "join" in output):

# input: 
#     list, optional separator, optional last separator.
# output: 
#     string, with separators if needed (built-in, or optional provided).
# examples also show:
#     the default parameter value for separator is ', ' and last separator is 'or'.
#     empty list returns an empty string.
#     a list with two elements will use the last separator.
# data structures: 
#     list, string.
# algorithm:
#     if empty list, return empty string.
#     if len(lst) == 1, return string of the value.
#     if len(lst) == 2, return f-string with last_sepr in-between list values.
#     if len(lst) > 2:
#         create a slice of everything but the last value
#         create an empty list to store string versions of those items
#             do that with a for loop
#         .join all of them with the separator, as a string, and save to another variable
#         return f-string with that variable, then the separator one more time, then the last separator, and then the remaining item in the input list

'''
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

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"
'''

# (My first algorithm was this, but wasn't working all the way):
#     if len(lst) > 2:
#         slice the list at [-2::-1] and save that to a first_part variable.
#         slice the list at [-2:] and save that to a last_part variable.
         
#         convert first_part to string.
#         run .replace(',', sepr) on first_part, reassign.
        
#         convert last_part to string.
#         run .replace(',', last_sepr) on last_part, reassign.
        
#         create result variable, concatenate the two strings maybe with something in the middle, save to result. return result.

#####

# 2 (Keep score):

# at start of execution, initialize player_score to 0 and computer_score to 0
# if detect_winner(board) == 'Player', increment player_score by 1
# if detect_winner(board) == 'Computer', increment computer_score by 1
# print scores after each game
# if player_score or computer_score == 5, print that they won the match
# reset both scores to 0
# no global variables

'''
def play_tic_tac_toe(player_marker, computer_marker, current_player):
    player_score = 0
    computer_score = 0

... ~ more code ~

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
'''

#####

# 3-5 (Computer AI defense, offense, refinements):

'''
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
'''

#####

# 5.3 (User chooses who goes first, or chooses random):

'''
X_MARKER = 'X'
O_MARKER = 'O'

def display_board(board, player_marker):
    os.system('clear')

    if player_marker == 'X':
        prompt(f"You are {X_MARKER}. Computer is {O_MARKER}.")
    else:
        prompt(f"Computer is {X_MARKER}. You are {O_MARKER}.")

... ~ more code ~

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

... ~ more code ~

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
'''

#####

# 6 (New play-again handling):

'''
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
'''

#####

# 7 (Improve game loop with choose_square and alternate_player):

'''
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
'''