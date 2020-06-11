from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min(count, num)
        if count == 0:
            raise ValueError("Only full decks can be dealt.")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled.")
        return shuffle(self.cards)

# d = Deck()
# print(d.deal_hand(2))
# print(d.deal_card())

d = Deck()
print(d)
d.shuffle()
print(d.count())

hand = d.deal_hand(5)
print(hand)