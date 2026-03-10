# 1:

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer_list = []
        
        for _ in range(size):
            self.buffer_list.append(None)
            
        self.next_slot = 0
        self.oldest_to_newest = [] # order of non-None items in buffer
            
    def put(self, item):
        overwritten = self.buffer_list[self.next_slot] # check for what's in next_slot
        
        if overwritten is not None: # for cases where buffer is full; self.next_slot will always point to an None slot if one exists.
            self.oldest_to_newest.pop(0)
                    
        self.buffer_list[self.next_slot] = item
        self.oldest_to_newest.append(item)
                    
        self.next_slot += 1
        if self.next_slot == self.size:
            self.next_slot = 0
        
    def get(self):
        if not self.oldest_to_newest:
            return None
        
        oldest_item = self.oldest_to_newest.pop(0)
        
        oldest_item_idx = self.buffer_list.index(oldest_item)
        self.buffer_list[oldest_item_idx] = None
       
        if all(item is None for item in self.buffer_list):
            self.next_slot = 0
            
        return oldest_item

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True

# 2:

import random

class GuessingGame:
    def reset(self):
        self.number = random.randint(1, 100)
        self.guesses = 7
    
    def play_round(self):
        print(f"You have {self.guesses} guesses remaining.")

        while self.guesses > 0:
            try:
                guess = int(input("Enter a number between 1 and 100: "))
            except ValueError:
                print("Invalid. Please enter an integer.")
                continue
            
            if guess not in range(1, 101):
                guess = int(input("Invalid guess. Enter a number between 1 and 100: "))
                continue
                
            elif guess < self.number:
                self.guesses -= 1
                print("Your guess is too low.")
                print(f"You have {self.guesses} guesses remaining.")
                continue
                
            elif guess > self.number:
                self.guesses -= 1
                print("Your guess is too high.")
                print(f"You have {self.guesses} guesses remaining.")
                continue

            else:
                print("That's the number!")
                print("You won!")
                break
                
        if self.guesses == 0:
            print("You have no more guesses. You lost!")
            print(f"The number was {self.number}.")

            
    def play(self):
        while True:
            self.reset()
            self.play_round()
            again = input("Play again? (y/n): ").strip().lower()
            if again == 'n':
                break
                
game = GuessingGame()
game.play()

# 3:

import random
import math

class GuessingGame:
    def __init__(self, low, high):
        self.low = low
        self.high = high
    
    def reset(self):
        self.number = random.randint(self.low, self.high)
        self.guesses = int(math.log2(self.high - self.low + 1)) + 1
    
    def play_round(self):
        print(f"You have {self.guesses} guesses remaining.")

        while self.guesses > 0:
            raw_input = input(f"Enter a number between {self.low} and {self.high}: ")
            try:
                guess = int(raw_input)
            except ValueError:
                print("Invalid. Please enter an integer.")
                continue
            
            if guess not in range(self.low, self.high + 1):
                print(f"Invalid guess. Enter a number between {self.low} and {self.high}: ")
                continue
                
            elif guess < self.number:
                print("Your guess is too low.")
                
            elif guess > self.number:
                print("Your guess is too high.")
                
            else:
                print("That's the number!")
                print("You won!")
                return
                
            self.guesses -= 1
            print(f"You have {self.guesses} guesses remaining.")

        print("You have no more guesses. You lost!")
        print(f"The number was {self.number}.")
            
    def play(self):
        while True:
            self.reset()
            self.play_round()
            again = input("Play again? (y/n): ").strip().lower()
            if again == 'n':
                break
                
game = GuessingGame(1, 1500)
game.play()

# 4:

class Card:
    RANK_VALUES = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    SUIT_VALUES = {"Diamonds": 1, "Clubs": 2, "Hearts": 3, "Spades": 4}
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __lt__(self, other):
        if not Card.RANK_VALUES[self.rank] == Card.RANK_VALUES[other.rank]:
            return Card.RANK_VALUES[self.rank] < Card.RANK_VALUES[other.rank]
        else:
            return Card.SUIT_VALUES[self.suit] < Card.SUIT_VALUES[other.suit]
    
    def __eq__(self, other):
        return Card.RANK_VALUES[self.rank] == Card.RANK_VALUES[other.rank] and Card.SUIT_VALUES[self.suit] == Card.SUIT_VALUES[other.suit]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
        
cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True

# 5:

import random

class Card:
    RANK_VALUES = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    SUIT_VALUES = {"Diamonds": 1, "Clubs": 2, "Hearts": 3, "Spades": 4}
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __lt__(self, other):
        if not Card.RANK_VALUES[self.rank] == Card.RANK_VALUES[other.rank]:
            return Card.RANK_VALUES[self.rank] < Card.RANK_VALUES[other.rank]
        else:
            return Card.SUIT_VALUES[self.suit] < Card.SUIT_VALUES[other.suit]
    
    def __eq__(self, other):
        return Card.RANK_VALUES[self.rank] == Card.RANK_VALUES[other.rank] and Card.SUIT_VALUES[self.suit] == Card.SUIT_VALUES[other.suit]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    def __init__(self):
        self.new_deck = []
        for rank in Deck.RANKS:
            for suit in Deck.SUITS:
                self.new_deck.append(Card(rank, suit))
        random.shuffle(self.new_deck)
    
    def draw(self):
        if self.new_deck:
            return self.new_deck.pop()
        else:
            for rank in Deck.RANKS:
                for suit in Deck.SUITS:
                    self.new_deck.append(Card(rank, suit))
            random.shuffle(self.new_deck)
            return self.new_deck.pop()
    
deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).

# 6:

import random

class Card:
    RANK_VALUES = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    SUIT_VALUES = {"Diamonds": 1, "Clubs": 2, "Hearts": 3, "Spades": 4}
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __lt__(self, other):
        if not Card.RANK_VALUES[self.rank] == Card.RANK_VALUES[other.rank]:
            return Card.RANK_VALUES[self.rank] < Card.RANK_VALUES[other.rank]
        else:
            return Card.SUIT_VALUES[self.suit] < Card.SUIT_VALUES[other.suit]
    
    def __eq__(self, other):
        return Card.RANK_VALUES[self.rank] == Card.RANK_VALUES[other.rank] and Card.SUIT_VALUES[self.suit] == Card.SUIT_VALUES[other.suit]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    def __init__(self):
        self._deck = []
        for rank in Deck.RANKS:
            for suit in Deck.SUITS:
                self._deck.append(Card(rank, suit))
        random.shuffle(self._deck)
    
    def draw(self):
        if self._deck:
            return self._deck.pop()
        else:
            for rank in Deck.RANKS:
                for suit in Deck.SUITS:
                    self._deck.append(Card(rank, suit))
            random.shuffle(self._deck)
            return self._deck.pop()

class PokerHand:
    def __init__(self, deck):
        self._hand = [deck.draw() for _ in range(5)]
        
        self.ranks = {}
        for card in self._hand:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
            
        self.suits = {}
        for card in self._hand:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def print(self):
        for card in self._hand:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
            return "High card"

    def _is_royal_flush(self):
        return 5 in self.suits.values() and {"Ace", "King", "Queen", "Jack", 10} == set(self.ranks.keys())

    def _is_straight_flush(self):
        numeric_ranks = [Card.RANK_VALUES[rank] for rank in self.ranks.keys()]
        return len(self.ranks) == 5 and max(numeric_ranks) - min(numeric_ranks) == 4 and 5 in self.suits.values()

    def _is_four_of_a_kind(self):
        return 4 in self.ranks.values()

    def _is_full_house(self):
        return 3 in self.ranks.values() and 2 in self.ranks.values()

    def _is_flush(self):
        return 5 in self.suits.values()

    def _is_straight(self):
        numeric_ranks = [Card.RANK_VALUES[rank] for rank in self.ranks.keys()]
        return len(self.ranks) == 5 and max(numeric_ranks) - min(numeric_ranks) == 4

    def _is_three_of_a_kind(self):
        return 3 in self.ranks.values()

    def _is_two_pair(self):
        list_of_values = list(self.ranks.values())
        if list_of_values.count(2) == 2:
            return True
        return False

    def _is_pair(self):
        return 2 in self.ranks.values()
    
hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")