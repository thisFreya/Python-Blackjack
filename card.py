# 
# Abstraction - A playing card, with value 1-13 (A,2->10,J,Q,K)
#               and suit (Hearts, Spades, Clubs, Diamonds).
#
# Rep Invariants:
#  1 <= value <= 13
#  1 <= suit <= 4

class Card():
    value = 0
    suit = 0

    # Checks the rep invariant of the data type.
    # When the given variables are not within
    # the given ranges, they are cropped back
    # to the edges of the range (i.e. -1 becomes
    # 1 in a range of 1 <= var <= 10).
    def checkRep(self):
        if(self.value > 13):
            self.value = 13
        elif(self.value < 1):
            self.value = 1
        if(self.suit > 4):
            self.suit = 4
        if(self.suit < 1):
            self.suit = 1

    # Card data type constructor.
    #
    # PARAM value : the value of the card. 1 <= value <= 13 when
    #               suit is defined. 1 <= value <= 52 iff
    #               suit is None. In this case, self.suit
    #               is defined by value % + 1, and
    #               self.value is defined by (value/4)+1.
    #
    # PARAM suit : the suit of the card.
    #              1 <= suit <= 4.
    def __init__(self, value, suit):
        if(suit is None):
            self.value = int(value / 4) + 1
            self.suit = value % 4 + 1
        else:
            self.value = value
            self.suit = suit

    # Getter for card value.
    #
    # RETURNS : the value of this card.
    def getValue(self):
        return self.value

    # Getter for card suit.
    #
    # RETURNS : the suit of the card.
    def getSuit(self):
        return self.suit

    # Getter for a combined number representing
    # this cards suit and value.
    #
    # RETURNS : a combined value of suit and number,
    #           1 <= num <= 52
    def getCardNum(self):
        return (self.value - 1) * 4 + (self.suit - 1)

    # Gets this card's value in string format.
    #
    # RETURNS : A string representation of this card's value.
    def valueString(self):
        if(self.value == 1):
            return "Ace"
        elif(self.value == 11):
            return "Jack"
        elif(self.value == 12):
            return "Queen"
        elif(self.value == 13):
            return "King"
        else:
            return str(self.value)

    # Gets this card's value in a shortened format,
    # at most two characters long.
    #
    # RETURNS : A string at most 2 characters long representing
    #           this card's value.
    def valueShort(self):
        if(self.value == 1 or self.value > 10):
            return self.valueString()[0]
        else:
            return str(self.value)

    # Gets this card's suit in a string format.
    #
    # RETURNS : A string representation of this card's suit.
    def suitString(self):
        if(self.suit == 1):
            return "Hearts"
        elif(self.suit == 2):
            return "Diamonds"
        elif(self.suit == 3):
            return "Clubs"
        elif(self.suit == 4):
            return "Spades"

    # Gets this card's suit in a shortened, one character long
    # format.
    #
    # RETURNS : A character representing this card's suit.
    def suitShort(self):
        return self.suitString()[0]

    # Gets a string representation of this card.
    #
    # RETURNS : This card represented as a string in the
    #           format [VALUE of SUIT].
    def toString(self):
        return "[" + str(self.valueString()) + " of " + str(self.suitString()) + "]";

    # Gets a shortened string representation of this card.
    #
    # RETURNS : This card represented as a string in the
    #           format [VV of S].
    def shortString(self):
        return "[" + str(self.valueShort()) + "-" + str(self.suitShort()) + "]";

    # Checks whether this and another card are, effectively, equal.
    #
    # PARAM otherCard : The other card to which this must be compared.
    #
    # RETURNS : true iff this card shares a value and suit with otherCard,
    #            and othercard is an instance of card.
    def equals(self, otherCard):
        try:
            return otherCard.getValue() == self.value and otherCard.getSuit() == self.suit
        except TypeError:
            return false
