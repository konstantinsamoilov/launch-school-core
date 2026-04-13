import random
import time

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] 
        RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] 

        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

class Participant:
    def __init__(self):
        self.hand = []

    def hit(self, deck):
        card = deck.deal()
        self.hand.append(card)

    def is_busted(self):
        return self.score() > 21

    def score(self):
        ranks = [card.rank for card in self.hand]
        total = 0

        for rank in ranks:
            if rank == 'A':
                total += 11
            elif rank in ['J', 'Q', 'K']:
                total += 10
            else:
                total += int(rank)

        num_aces = ranks.count('A')

        while total > 21 and num_aces > 0:
            total -= 10
            num_aces -= 1

        return total
    
    def reset_hand(self):
        self.hand = []

class Player(Participant):
    def __init__(self):
        super().__init__()
        self.funds = 5

class Dealer(Participant):
    def __init__(self):
        super().__init__()

class TwentyOneGame:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()

    def _start(self):
        self.player.reset_hand()
        self.dealer.reset_hand()

        self.deck = Deck()
        self._deal_hands()
        self._show_player_hand()
        self._show_dealer_card()
        self._player_turn()

        if not self.player.is_busted():
            self._dealer_turn()

        self._display_result_and_funds()

    def _deal_hands(self):
        self.player.hand.append(self.deck.deal())
        self.dealer.hand.append(self.deck.deal())
        self.player.hand.append(self.deck.deal())
        self.dealer.hand.append(self.deck.deal())

    def _show_player_hand(self):
        print(f"Your hand is:")
        for player_card in self.player.hand:
            print(f"{player_card.rank} of {player_card.suit}")
        print(f"{self.player.score()} points.")
        print('')

    def _show_dealer_card(self):
        print(f"The dealer's first card is {self.dealer.hand[0].rank}"
              f" of {self.dealer.hand[0].suit}.")
        print('')

    def _player_turn(self):
        while True:
            choice = self._get_player_choice()

            if choice == 'h':
                self.player.hit(self.deck)
                print('')
                print("You hit.")
                self._show_player_hand()

                if self.player.is_busted():
                    print("You busted!")
                    break

            elif choice == 's':
                print('')
                print("You stay.")
                print('')
                break

    def _dealer_turn(self):
        print(f"The dealer's hand is:")
        for dealer_card in self.dealer.hand:
            print(f"{dealer_card.rank} of {dealer_card.suit}")
        print(f"{self.dealer.score()} points.")

        while self.dealer.score() < 17:
            time.sleep(1)
            self.dealer.hit(self.deck)

            print('')
            print('Dealer hits. Now its hand is:')
            for dealer_card in self.dealer.hand:
                print(f"{dealer_card.rank} of {dealer_card.suit}")
            print(f"{self.dealer.score()} points.")

        if self.dealer.is_busted():
            print('')
            print(f"{self.dealer.score()}. Dealer busts!")
        else:
            print('')
            print("Dealer stays.")

    def display_welcome_message(self):
        print('')
        print("Welcome to 21!")
        print('')

    def display_goodbye_message(self):
        print("Thanks for playing!")

    def _display_result_and_funds(self):
        player_score = self.player.score()
        dealer_score = self.dealer.score()

        print('')
        print(f"Your score: {player_score}")
        print(f"Dealer's score: {dealer_score}")
        print('')

        if self.player.is_busted():
            print("You busted. Dealer wins.")
            self.player.funds -= 1
        elif self.dealer.is_busted():
            print("You win!")
            self.player.funds += 1
        elif player_score > dealer_score:
            print("You win!")
            self.player.funds += 1
        elif dealer_score > player_score:
            print("Dealer wins.")
            self.player.funds -= 1
        else:
            print("It's a tie!")

        print(f"You now have ${self.player.funds}.")
        print('')

    def _play_again(self):
        while True:
            again = input("Want to play again? (y/n): ").lower()
            if again == 'y':
                return True
            if again == 'n':
                return False
            print("Invalid input.")

    def _match_over_due_to_funds(self):
        if self.player.funds == 0:
            print("You're out of funds! The match is over.")
            return True
        
        if self.player.funds == 10:
            print("You're rich! The match is over.")
            return True
        
        return False

    def _get_player_choice(self):
        while True:
            choice = input("Hit or stay? H to hit, S to stay: ").lower()
            if choice in ['h', 's']:
                return choice
            print("Invalid choice.")

    def play(self):
        while True:
            game._start()

            if game._match_over_due_to_funds():
                break

            if not game._play_again():
                break

game = TwentyOneGame()
game.display_welcome_message()
game.play()
game.display_goodbye_message()