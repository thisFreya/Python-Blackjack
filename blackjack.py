#################################################
#                  Blackjack                    #
#################################################
#
# Author: Tyler Heim
# Github: thisTyler
# Constructed for the purpose of learning and
# practicing Python in my free time.
#
# Suits are valued in integer form as follows:
#      Hearts   = 0
#      Diamonds = 1
#      Clubs    = 2
#      Spades   = 3
#
# Card integers must be formatted for:
#      int  = 4*(card value - 1)
#      suit = int % 4
#
# Win condition conventions:
#  0.0  : Full loss of money.
#  1.0  : Pushed. Bet is returned.
#  1.5  : Blackjack. Bet payed 3:2.
#  2.0  : Win. Bet is payed 2:1.
#  3.0  : Split hands, one pushed, the other won. Bet payed 3:2.
#  3.25 : Split hands, one pushed, the other lost. Bet payed 1:2.
#  3.5  : Split hands, both pushed. Bet returned.
#  3.75 : Split hands, one won, the other lost. Bet returned.
#  3.8  : Split hands, both lost. Bet is lost.
#  3.9  : Split hands, both won. Bet payed 2:1.
#  4.0  : Split hands, both got blackjack. Bet payed 3:2.
#  4.5  : Split hands, one blackjack, other lost. Bet payed 3:4.
#  4.75 : Split hands, one blackjack, other pushed. Bet payed 5:4.
#  5.0  : Split hands, one blackjack, other won. Bet payed 7:4.
#  6.0  : Won on double down, original bet pays back 3:1.
#  6.5  : Lost on double down, original bet is lost twice over.
#  6.75 : Pushed on double down. Bet is returned.

import random

# Evaluates the point value of a hand of cards.
# All face cards are valued at 10 points,
# All numerical points are face value,
# Excepting the Ace, which is valued
# at 11 points until the hand's total surpasses
# 21 points, in which case it is valued at 1 point.
#
# PARAM hand : A list of integers (valued between 1 and 52, inclusive)
#              representing cards.
#              Each card integer must follow header conventions.
# RETURNS : An integer representing the value of the given hand.
def evaluateHand(hand):
    sum = 0
    for i in hand:
        if(int(i/4) + 1 <= 10):
            sum += int(i / 4) + 1
        else:
            sum += 10

    if(sum <= 11):
        for i in hand:
            if(int(i/4) + 1 == 1):
                sum += 10
                break
    return sum

# Gets a readout representing a card in the format:
# [Value of Suit] (ex. [King of Hearts])
#
# PARAM card : an integer representing a card.
#              The integer must follow header
#              conventions.
#
# RETURNS : A string representing the given card.
def printCard(card):
    value = int(card / 4) + 1
    suit = card % 4
    rString = ""
    if(value == 1):
        rString += "Ace"
    elif(value == 11):
        rString += "Jack"
    elif(value == 12):
        rString += "Queen"
    elif(value == 13):
        rString += "King"
    else:
        rString += str(value)

    rString += " of "

    if(suit == 0):
        rString += "Hearts"
    elif(suit == 1):
        rString += "Diamonds"
    elif(suit == 2):
        rString += "Clubs"
    elif(suit == 3):
        rString += "Spades"

    return rString

# Gets a readout representing the cards
# in the given hand.
#
# PARAM hand : A list of integers
#              representing cards in the
#              player's hand. Card integers
#              must follow header conventions.
#
# RETURNS : A string printout of the player's hand.
def printPlayerHand(hand):
    rString = "Your Hand: "
    for i in hand:
        rString += "["
        rString += printCard(i)
        rString += "]"
    return rString

# Gets a readout representing the cards
# in the given hands. Prints the first
# hand followed by the second on separate
# lines.
#
# PARAM hand1 : A list of integers
#              representing cards in the
#              player's first hand. Card integers
#              must follow header conventions.
# PARAM hand2 : A list of integers
#              representing cards in the
#              player's second hand. Card integers
#              must follow header conventions.
#
# RETURNS : A string printout of the player's hands.
def printSplitHand(hand1, hand2):
    rString = "Your hands: \n1: "
    for i in hand1:
        rString += "["
        rString += printCard(i)
        rString += "]"
    rString += "\n2: "
    for i in hand2:
        rString += "["
        rString += printCard(i)
        rString += "]"
    return rString

# Gets a readout representing the cards
# in the given dealer's hand. Can
# obscure the first card if necesarry.
#
# PARAM hand : A list of integers
#              representing cards in the
#              dealer's hand. Card integers
#              must follow header conventions.
# PARAM blank : A boolean that reads TRUE iff
#               the dealer's first card should not
#               be revealed, instead being displayed
#               as "[]".
#
# RETURNS : A string printout of the dealer's hand.
def printDealerHand(hand, blank):
    rString = "Dealer's Hand: "
    for i in range(len(hand)):
        if(i == 0 and blank):
            rString += "[]"
        else:
            rString += "["
            rString += printCard(hand[i])
            rString += "]"
    return rString

# Gets a new random card, will not deal
# the same card twice. Dealt card
# must be added to dealtCards after
# the fact to avoid redealing.
#
# PARAM dealtCards : A list of card integers
#                    previously dealt out using
#                    this function or others.
#                    These cards will not be dealt
#                    again. Integers must follow
#                    header conventions.
#
# RETURNS : an integer representing a card
#           following header conventions.
#           This integer is not contained in
#           dealtCards.
def dealCard(dealtCards):
    card = random.randint(1, 52)
    sentinel = True
    while(sentinel):
        sentinel = False
        for i in dealtCards:
            if(i == card):
                sentinel = True
                break
        card = random.randint(1, 52)
    return card

# Plays a round of Blackjack. Deals the cards,
# handles the moves, and determines whether the
# player won or lost, and by how much their bet
# is returned.
#
# PARAM canDouble : Whether the player has
#                   sufficient money available
#                   to double down on their bet.
#
# RETURNS : A float representing the win state
#           of the game. The conventions for this
#           are outlined in the header.
def playRound(canDouble):
    playerHand = []
    splitHand = []
    dealerHand = []
    dealtCards = []

    for i in range(2):
        card = dealCard(dealtCards)
        playerHand.append(card)
        dealtCards.append(card)
        card = dealCard(dealtCards)
        dealerHand.append(card)
        dealtCards.append(card)

    print(printDealerHand(dealerHand, True))
    print(printPlayerHand(playerHand))
    print("Your current total is " + str(evaluateHand(playerHand)))

    win = 0.0

    if(evaluateHand(playerHand) == 21):
        print("Blackjack!")
        win = 1.5
    else:
        inString = ""
        if(canDouble):
            if(int(playerHand[0] / 4) == int(playerHand[1] / 4)):
                inString = input("Do you want to (h)it', (s)tand, (d)ouble down, or (sp)lit? ")
            else:
                inString = input("Do you want to (h)it, (s)tand, or (d)ouble down? ")
        else:
            if(int(playerHand[0] / 4) == int(playerHand[1] / 4)):
                inString = input("Do you want to (h)it', (s)tand, or (sp)lit? ")
            else:
                inString = input("Do you want to (h)it or (s)tand? ")
        print()
        inString = inString.lower()

        if(inString == "sp"):#----------------------Beginning of split hand------------------------------------------------------
            store = playerHand[1]
            splitHand.append(store)
            card = dealCard(dealtCards)
            dealtCards.append(card)
            playerHand[1] = card
            card = dealCard(dealtCards)
            dealtCards.append(card)
            splitHand.append(card)
            win = 3.80
            playerBlackjack = False
            splitBlackjack = False

            print(printSplitHand(playerHand, splitHand))
            if(evaluateHand(playerHand) == 21):
                print("Hand 1 has blackjack!")
                playerBlackjack = True
            else:
                inString = input("Hand 1: Do you want to (h)it or (s)tand? ")
                print()
                while(inString != 's'):
                    card = dealCard(dealtCards)
                    playerHand.append(card)
                    dealtCards.append(card)
                    print(printPlayerHand(playerHand))
                    print("Your new total is " + str(evaluateHand(playerHand)))
                    if(evaluateHand(playerHand) > 21):
                        print("Bust!")
                        break
                    inString = input("Hand 1: Do you want to (h)it or (s)tand? ")
                    print()
                    inString = inString.lower()

            print(printSplitHand(playerHand, splitHand))
            if(evaluateHand(splitHand) == 21):
                print("Hand 2 has blackjack!")
                splitBlackjack = True
            else:
                inString = input("Hand 2: Do you want to (h)it or (s)tand? ")
                print()
                while(inString != 's'):
                    card = dealCard(dealtCards)
                    splitHand.append(card)
                    dealtCards.append(card)
                    print(printPlayerHand(splitHand))
                    print("Your new total is " + str(evaluateHand(splitHand)))
                    if(evaluateHand(playerHand) > 21):
                        print("Bust!")
                        break
                    inString = input("Hand 2: Do you want to (h)it or (s)tand? ")
                    print()
                    inString = inString.lower()

            print()
            if(not(playerBlackjack) or not(splitBlackjack)):
                while(evaluateHand(dealerHand) < 18):
                    card = dealCard(dealtCards)
                    dealerHand.append(card)
                    dealtCards.append(card)
                    print("Dealer hits.")
                    if(evaluateHand(dealerHand) > 21):
                        print(printDealerHand(dealerHand, False))
                        print("Dealer busts!")
                    else:
                        print(printDealerHand(dealerHand, True))

            if(not(playerBlackjack) and not(splitBlackjack)):
                if(evaluateHand(dealerHand) <= 21):
                    if(evaluateHand(playerHand) <= 21 and evaluateHand(splitHand) <= 21):
                        if(evaluateHand(playerHand) == evaluateHand(dealerHand) and evaluateHand(splitHand) == evaluateHand(dealerHand)):
                            win = 3.50
                        elif((evaluateHand(playerHand) == evaluateHand(dealerHand) and evaluateHand(splitHand) < evaluateHand(dealerHand)) or (evaluateHand(splitHand) == evaluateHand(dealerHand) and evaluateHand(playerHand) < evaluateHand(dealerHand))):
                            win = 3.25
                        elif((evaluateHand(playerHand) == evaluateHand(dealerHand) and evaluateHand(splitHand) > evaluateHand(dealerHand)) or (evaluateHand(splitHand) == evaluateHand(dealerHand) and evaluateHand(playerHand) > evaluateHand(dealerHand))):
                            win = 3.0
                        elif((evaluateHand(playerHand) > evaluateHand(dealerHand) and evaluateHand(splitHand) < evaluateHand(dealerHand)) or (evaluateHand(splitHand) > evaluateHand(dealerHand) and evaluateHand(playerHand) < evaluateHand(dealerHand))):
                            win = 3.75
                        elif(evaluateHand(playerHand) < evaluateHand(dealerHand) and evaluateHand(splitHand) < evaluateHand(dealerHand)):
                            win = 3.80
                        elif(evaluateHand(playerHand) > evaluateHand(dealerHand) and evaluateHand(splitHand) > evaluateHand(dealerHand)):
                            win = 3.90
                    elif(evaluateHand(playerHand) <= 21 or evaluateHand(splitHand) <= 21):
                        if(evaluateHand(playerHand) <= 21):
                            if(evaluateHand(splitHand) > evaluateHand(dealerHand)):
                                win = 3.75
                            elif(evaluateHand(splitHand) == evaluateHand(dealerHand)):
                                win = 3.25
                        else:
                            if(evaluateHand(playerHand) > evaluateHand(dealerHand)):
                                win = 3.75
                            elif(evaluateHand(playerHand) == evaluateHand(dealerHand)):
                                win = 3.25
                else:
                    if(evaluateHand(playerHand) <= 21 and evaluateHand(splitHand) <= 21):
                        win = 3.9
                    elif(evaluateHand(playerHand) <= 21 or evaluateHand(splitHand) <= 21):
                        win = 3.75
            else:
                if(playerBlackjack and splitBlackjack):
                    win = 4.0
                elif(playerBlackjack):
                    if(evaluateHand(dealerHand) > 21):
                        win = 5.0
                    elif(evaluateHand(splitHand) <= 21):
                        if(evaluateHand(splitHand) > evaluateHand(dealerHand)):
                            win = 5.0
                        elif(evaluateHand(splitHand) == evaluateHand(dealerHand)):
                            win = 4.75
                        else:
                            win = 4.5
                    else:
                        win = 4.5
                elif(splitBlackjack):
                    if(evaluateHand(dealerHand) > 21):
                        win = 5.0
                    elif(evaluateHand(playerHand) <= 21):
                        if(evaluateHand(playerHand) > evaluateHand(dealerHand)):
                            win = 5.0
                        elif(evaluateHand(playerHand) == evaluateHand(dealerHand)):
                            win = 4.75
                        else:
                            win = 4.5
                    else:
                        win = 4.5
            print()

            if(evaluateHand(playerHand) <= 21):
                print(printPlayerHand(playerHand) + " scoring " + str(evaluateHand(playerHand)))
            else:
                print(printPlayerHand(playerHand) + " busts.")

            if(evaluateHand(splitHand) <= 21):
                print(printPlayerHand(splitHand) + " scoring " + str(evaluateHand(splitHand)))
            else:
                print(printPlayerHand(splitHand) + " busts.")

            if(evaluateHand(dealerHand) <= 21):
                print(printDealerHand(dealerHand, False) + " scoring " + str(evaluateHand(dealerHand)))
            else:
                print(printDealerHand(dealerHand) + " busts.")
        else: #---------------Beginning of single hand ------------------------------------------------------------------------------------------------------
            if(inString != "d"):
                while(inString != "s"):
                    card = dealCard(dealtCards)
                    playerHand.append(card)
                    dealtCards.append(card)
                    print(printPlayerHand(playerHand))
                    print("Your new total is " + str(evaluateHand(playerHand)))
                    if(evaluateHand(playerHand) > 21):
                        print("Bust!")
                        break
                    inString = input("Do you want to (h)it or (s)tand? ")
                    print()
                    inString = inString.lower()
                print()

                while(evaluateHand(dealerHand) < 18):
                    card = dealCard(dealtCards)
                    dealerHand.append(card)
                    dealtCards.append(card)
                    print("Dealer hits.")
                    if(evaluateHand(dealerHand) > 21):
                        print(printDealerHand(dealerHand, False))
                        print("Dealer busts!")
                    else:
                        print(printDealerHand(dealerHand, True))

                if(evaluateHand(dealerHand) <= 21):
                    if(evaluateHand(playerHand) <= 21 and evaluateHand(playerHand) >= evaluateHand(dealerHand)):
                        win = 2.0
                    elif(evaluateHand(playerHand) <= 21 and evaluateHand(playerHand) == evaluateHand(dealerHand)):
                        win = 1.0
                else:
                    if(evaluateHand(playerHand) <= 21):
                        win = 2.0
                    else:
                        win = 0.0
                print()
            else:
                win = 6.5
                card = dealCard(dealtCards)
                playerHand.append(card)
                dealtCards.append(card)
                print(printPlayerHand(playerHand))
                print("Your new total is " + str(evaluateHand(playerHand)) + "\n")

                while(evaluateHand(dealerHand) < 18):
                    card = dealCard(dealtCards)
                    dealerHand.append(card)
                    dealtCards.append(card)
                    print("Dealer hits.")
                    if(evaluateHand(dealerHand) > 21):
                        print(printDealerHand(dealerHand, False))
                        print("Dealer busts!")
                    else:
                        print(printDealerHand(dealerHand, True))

                if(evaluateHand(dealerHand) <= 21):
                    if(evaluateHand(playerHand) <= 21 and evaluateHand(playerHand) >= evaluateHand(dealerHand)):
                        win = 6.0
                    elif(evaluateHand(playerHand) <= 21 and evaluateHand(playerHand) == evaluateHand(dealerHand)):
                        win = 6.75
                else:
                    if(evaluateHand(playerHand) <= 21):
                        win = 6.0
                    else:
                        win = 6.5
                print()

            if(evaluateHand(playerHand) <= 21):
                print(printPlayerHand(playerHand) + " scoring " + str(evaluateHand(playerHand)))
            else:
                print(printPlayerHand(playerHand) + " busts.")
            if(evaluateHand(dealerHand) <= 21):
                print(printDealerHand(dealerHand, False) + " scoring " + str(evaluateHand(dealerHand)))
            else:
                print(printDealerHand(dealerHand, False) + " busts.")
    return win

# Plays a game of Blackjack. This handles the metagame,
# i.e. the betting, the wallet, and the returns. Only
# stops if you are broke or indicate you don't want to play again.
#
# PARAM wallet : A number representing the amount
#                of money you begin the game with.
#
def playBlackjack(wallet):
    playAgain = True
    while(playAgain and wallet > 0):
        print("You have $" + "{:.2f}".format(wallet))
        bet = float(input("Place your bet. $"))
        while(bet > wallet):
            bet = float(input("You don't have enough money for that bet. \nWhat's your bet? $"))
        win = 0.0
        wallet -= bet
        if(wallet >= bet):
            win = playRound(True)
        else:
            win = playRound(False)
        print()
        if(win == 2.0):
            print("You win! Your bet is payed 2:1 and you win $" + "{:.2f}".format(bet * 2))
            wallet += 2 * bet
        elif(win == 1.5):
            print("You got blackjack! Your bet is payed 3:2 and you win $" + "{:.2f}".format(bet * 1.5))
            wallet += 1.5 * bet
        elif(win == 1.0):
            print("You pushed. Your bet is returned. ")
            wallet += bet
        elif(win == 0.0):
            print("You lost. The dealer keeps your bet. ")
        elif(win == 3.0):
            print("One hand pushed and the other won. Your bet payed 3:2 and you win $" + "{:.2f}".format(bet * 1.5))
            wallet += 1.5 * bet
        elif(win == 3.25):
            print("One hand pushed and the other lost. Half your bet is returned - $" + "{:.2f}".format(bet * .5))
            wallet += .5 * bet
        elif(win == 3.5):
            print("Both hands pushed. Your bet is returned - $" + "{:.2f}".format(bet))
            wallet += bet
        elif(win == 3.75):
            print("One hand won and the other lost. Your original bet is returned - $" + "{:.2f}".format(bet))
            wallet += bet
        elif(win == 3.8):
            print("Both hands lost. The dealer keeps your bet. ")
        elif(win == 3.9):
            print("Both hands won! Your bet is payed 2:1 and you win $" + "{:.2f}".format(bet * 2))
            wallet += bet*2
        elif(win == 4.0):
            print("Both hands got blackjack, so your bet is payed 3:2 and you win $" + "{:.2f}".format(bet * 1.5))
            wallet += 1.5 * bet
        elif(win == 4.5):
            print("One hand got blackjack and the other lost, so your bet is payed 3:4, returning you $" + "{:.2f}".format(bet * .75))
            wallet += .75 * bet
        elif(win == 4.75):
            print("One hand got blackjack and the other pushed, so your bet is payed 5:4, and you win $" + "{:.2f}".format(bet * 1.25))
            wallet += 1.25 * bet
        elif(win == 5.0):
            print("One hand got blackjack and the other won, so your bet is payed 7:4 and you win $" + "{:.2f}".format(bet * 1.75))
            wallet += 1.75 * bet
        elif(win == 6.0):
            print("You won on a double down. Your doubled $" + "{:.2f}".format(bet) + " bet pays back $" + "{:.2f}".format(bet * 4))
            wallet += 3 * bet
        elif(win == 6.5):
            print("You lost on a double down. Your doubled $" + "{:.2f}".format(bet) + " bet is lost.")
            wallet -= bet
        elif(win == 6.75):
            print("You pushed on a double down. Your doubled bet was returned.")
        if(wallet > 0):
            cont = input("Do you want to play again? (Y/N) ").lower()
            if(cont == "n"):
                playAgain = False
        else:
            print("You're broke. Sorry.")
            playAgain = False
        print()
        print("------------------------------")
        print()

playBlackjack(5.00)
input()
