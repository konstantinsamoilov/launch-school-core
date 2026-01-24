'''
1. Initialize deck
2. Deal cards to player and dealer

3. Player turn: hit or stay
3.5. Repeat until bust or stay
4. If player busts, dealer wins

5. Dealer turn: hit
5.5. Repeat until total >= 17
6. If dealer busts, player wins

7. Compare cards and declare winner

Data structure:
Deck: List for suits, list for ranks
Player's cards: List
Dealer's cards: List

Calculating Aces:
For the initial 2-card hand, Aces are 11.
Aces in hand may have to be tracked.
When player/dealer gets more cards:
    If the total of the hand is over 21, one Ace becomes 1.
        If the total of the hand is still over 21
        and there are more Aces, a second Ace becomes 1.
            Etc...

Player turn:
After player sees their two cards and one dealer card:
Ask player to hit or stay.
    If player hits:
        Keep doing that if player hits.
            If player busts:
                Player loses.
    If player stays:
        Dealer turn begins.

Dealer turn:
If player busts, dealer wins, no turn.
If player stays and dealer is >= 17:
    Dealer stays
If player stays and dealer is < 17:
    Dealer hits
    Dealer continues to hit until they are >= 17 or bust

Result function:
If player busts, dealer wins
If player stays and dealer busts, player wins
If both stay, whoever has the highest card value wins
Returns name of winner

Display_result function:
Takes name of winner from result
Prints "{name} wins the game."

#####
Not many functions here, that's the biggest flaw.

I don't display totals during the game because
a part of 21/BJ is thinking about it yourself.

Totals are displayed after a game ends.
#####
'''
TOP_VALUE = 21
DEALER_STAYS = 17

import random

def calculate_total(cards):
    ranks = [card[1] for card in cards]
    total = 0

    for rank in ranks:
        if rank == 'A':
            total += 11
        elif rank in ('K', 'Q', 'J'):
            total += 10
        else:
            total += int(rank)

    aces_11 = ranks.count('A')

    while total > TOP_VALUE and aces_11 > 0:
        total -= 10
        aces_11 -= 1

    return total

def prompt(message):
    print(f'==> {message}')

player_wins = 0
dealer_wins = 0

while True:
    deck = [['Clubs', '2'], ['Clubs', '3'], ['Clubs', '4'],
            ['Clubs', '5'], ['Clubs', '6'], ['Clubs', '7'],
            ['Clubs', '8'], ['Clubs', '9'], ['Clubs', '10'],
            ['Clubs', 'J'], ['Clubs', 'Q'], ['Clubs', 'K'],
            ['Clubs', 'A'], ['Diamonds', '2'], ['Diamonds', '3'],
            ['Diamonds', '4'], ['Diamonds', '5'], ['Diamonds', '6'],
            ['Diamonds', '7'], ['Diamonds', '8'], ['Diamonds', '9'],
            ['Diamonds', '10'], ['Diamonds', 'J'], ['Diamonds', 'Q'],
            ['Diamonds', 'K'], ['Diamonds', 'A'], ['Hearts', '2'],
            ['Hearts', '3'], ['Hearts', '4'], ['Hearts', '5'],
            ['Hearts', '6'], ['Hearts', '7'], ['Hearts', '8'],
            ['Hearts', '9'], ['Hearts', '10'], ['Hearts', 'J'],
            ['Hearts', 'Q'], ['Hearts', 'K'], ['Hearts', 'A'],
            ['Spades', '2'], ['Spades', '3'], ['Spades', '4'],
            ['Spades', '5'], ['Spades', '6'], ['Spades', '7'],
            ['Spades', '8'], ['Spades', '9'], ['Spades', '10'],
            ['Spades', 'J'], ['Spades', 'Q'], ['Spades', 'K'],
            ['Spades', 'A']]

    random.shuffle(deck)

    player_hand = [deck.pop(0), deck.pop(0)]
    dealer_hand = [deck.pop(0), deck.pop(0)]

    player_total = calculate_total(player_hand)

    prompt('Welcome to Twenty-One.')
    prompt('You can play a match, until you or the dealer have 3 wins.')
    prompt(f'Your hand is {player_hand[0][1]} of {player_hand[0][0]}'
           f' and {player_hand[1][1]} of {player_hand[1][0]}.')
    prompt(f"The dealer's first card is {dealer_hand[0][1]}"
           f" of {dealer_hand[0][0]}. Card 2 is face down.")

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

    if player_total > TOP_VALUE:
        prompt("Dealer wins.")

    else:
        prompt("Now it's dealer's turn. The dealer's hand is:")
        for dealer_card in dealer_hand:
            prompt(f'{dealer_card[1]} of {dealer_card[0]}.')

        dealer_total = calculate_total(dealer_hand)

        while dealer_total < DEALER_STAYS:
            dealer_hand.append(deck.pop(0))
            dealer_total = calculate_total(dealer_hand)

            prompt('Dealer hits. Now its hand is:')
            for dealer_card in dealer_hand:
                prompt(f'{dealer_card[1]} of {dealer_card[0]}.')

        if dealer_total > TOP_VALUE:
            prompt(f"{dealer_total}. Dealer busts! You win.")
            player_wins += 1

        else:
            prompt("Dealer stays.")

            if player_total > dealer_total:
                prompt(f"You win! You have {player_total}, Dealer has {dealer_total}.")
                player_wins += 1

            elif dealer_total > player_total:
                prompt(f"Dealer wins! Dealer has {dealer_total}, "
                        f"you have {player_total}.")
                dealer_wins += 1

            else:
                prompt(f"It's a tie. You and Dealer have {player_total}.")

    prompt(f"You have {player_wins} wins. Dealer has {dealer_wins} wins.")

    if player_wins == 3:
        prompt("You've won the match! Resetting your and dealer's wins to 0.")
        player_wins = 0
        dealer_wins = 0

    elif dealer_wins == 3:
        prompt("Dealer has won the match. Resetting dealer's and your wins to 0.")
        player_wins = 0
        dealer_wins = 0

    play_again = input("Play again? (Y/y or N/n): ").lower()

    while play_again not in ('n', 'y'):
        play_again = input("Not a valid choice. Y/y to play again, N/n to exit: ").lower()

    if play_again == 'n':
        break

    if play_again == 'y':
        continue

prompt('Thanks for playing!')