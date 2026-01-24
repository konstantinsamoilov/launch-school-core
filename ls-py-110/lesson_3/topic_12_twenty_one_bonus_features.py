# 1 (Minimizing calls to total):

# Made one small change (took out calculation from a "stay" block
# and put it before the start of the main loop. The rest was ok.)

# 2 (continue vs break):

# We use 'continue' mid-loop to skip through the rest of the program
# and start another loop from the beginning.

# And we use 'break' to terminate the loop completely, so
# you put that at the very end of program code, and if user chooses
# not to break, it naturally restarts the loop anyway.

# 3 (Grand output for all round endings in the LS solution):

# We just have to move it to display_results.

'''
def display_results(dealer_cards, player_cards):
    result = detect_result(dealer_cards, player_cards)

    match result:
        case 'PLAYER_BUSTED':
            prompt('You busted! Dealer wins!')
        case 'DEALER_BUSTED':
            prompt('Dealer busted! You win!')
        case 'PLAYER':
            prompt('You win!')
        case 'DEALER':
            prompt('Dealer wins!')
        case _:
            prompt("It's a tie!")

    print('==============')
    prompt(f"Dealer has {hand(dealer_cards)}, for a total of: {total(dealer_cards)}")
    prompt(f"Player has {hand(player_cards)}, for a total of: {total(player_cards)}")
    print('==============')
'''

# 4 (Best of Five):

# Back to my code.

'''
player_wins = 0
dealer_wins = 0

# Then various lines of player_wins / dealer_wins += 1
# And near the end:

    prompt(f"You have {player_wins} wins. Dealer has {dealer_wins} wins.")

    if player_wins == 3:
        prompt("You've won the match! Resetting your and dealer's wins to 0.")
        player_wins = 0
        dealer_wins = 0

    elif dealer_wins == 3:
        prompt("Dealer has won the match. Resetting dealer's and your wins to 0.")
        player_wins = 0
        dealer_wins = 0
'''

# 5 (More constants):

# TOP_VALUE = 21
# DEALER_STAYS = 17

# 6 (Improved input handling):

'''
    while True:
        hit_or_stay = input('Do you want to hit or stay?' \
                    ' Hit/H to hit, Stay/S to stay: ').lower()

        if hit_or_stay in ('hit', 'h'):
            player_hand.append(deck.pop(0))
            player_total = calculate_total(player_hand)

            prompt('Hit. Now your hand is:')
            for player_card in player_hand:
                prompt(f'{player_card[1]} of {player_card[0]}.')

            if player_total > TOP_VALUE:
                prompt(f"Your total is {player_total}. Bust!")
                dealer_wins += 1
                break

        elif hit_or_stay in ('stay', 's'):
            prompt(f"You stay. Your total is {player_total}.")
            break

        else:
            prompt("Invalid choice.")
'''

'''
    play_again = input("Play again? (Y/y or N/n): ").lower()

    while play_again not in ('n', 'y'):
        play_again = input("Not a valid choice. Y/y to play again, N/n to exit: ").lower()

    if play_again == 'n':
        break

    if play_again == 'y':
        continue

prompt('Thanks for playing!')
'''