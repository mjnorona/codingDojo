import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print "{} of {}".format(self.suit, self.val)

class Deck(object):
    def __init__(self):
        self.cards = self.build()


    def build(self):
        listCards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        listSuits = ["Diamonds", "Hearts", "Spades", "Clovers"]
        self.cards = []
        for i in range(0, len(listSuits)):
            for j in range(0, len(listCards)):
                self.cards.append(Card(listCards[j], listSuits[i]))
        return self.cards

    def showDeck(self):
        print "Current Deck: "
        for i in range(0, len(self.cards)):
            self.cards[i].show()
        print ""
        return self

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            number = random.randint(0, i)
            temp = self.cards[i]
            self.cards[i] = self.cards[number]
            self.cards[number] = temp
        return self

    def draw(self, *players):
        for i in range(0, len(players)):
            hand = []
            if len(self.cards) >= 5:
                hand = self.cards[len(self.cards) - 5: len(self.cards)]
                self.cards = self.cards[0: len(self.cards) - 5]
            else:
                print "Not enough cards left"
            players[i].getHand(hand)
        return self

    def reset(self, *args):
        for i in range(0, len(args)):
            args[i].hand = []
        self.cards = self.build()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def getHand(self, newHand):
        self.hand = newHand
        return self

    def displayHand(self):
        print self.name +  "'s hand: "
        for i in range(0, len(self.hand)):
            self.hand[i].show()
        print ""
        return self

deck = Deck()
deck.showDeck()

deck.shuffle()
deck.showDeck()


player1 = Player("Marcus")
player2 = Player("Jeremy")

deck.draw(player1, player2)

deck.showDeck()
player1.displayHand()
player2.displayHand()

deck.reset(player1, player2)

deck.showDeck()
player1.displayHand()
player2.displayHand()


