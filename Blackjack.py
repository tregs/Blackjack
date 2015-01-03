# couldn't be fucked implementing aces properly so I just assigned their value as 11.  I'll redo this once I learn classes and do it properly.

import random

complete_deck = [
'S-2', 'S-3', 'S-4', 'S-5', 'S-6', 'S-7', 'S-8', 'S-9', 'S-10', 'S-J', 'S-Q', 'S-K', 'S-A',
'C-2', 'C-3', 'C-4', 'C-5', 'C-6', 'C-7', 'C-8', 'C-9', 'C-10', 'C-J', 'C-Q', 'C-K', 'C-A',
'D-2', 'D-3', 'D-4', 'D-5', 'D-6', 'D-7', 'D-8', 'D-9', 'D-10', 'D-J', 'D-Q', 'D-K', 'D-A',
'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'H-7', 'H-8', 'H-9', 'H-10', 'H-J', 'H-Q', 'H-K', 'H-A'
]

print """
Welcome to big bogan blackjack! 

How to play: Cards are shown in the form Suit-Number, for example,
the king of spades is shown as S-K. The game will prompt you for choices,
it's pretty simple. Good luck!
"""

decks = int(raw_input("How many decks would you like to play with? > "))

player_hand = []
dealer_hand = []

#takes the number of decks from the user and builds a playing deck with that number of 52 card decks in it.
def build_deck(decks):
	deck = []
	building_deck = complete_deck * decks
	for j in range(0, len(building_deck)):
		deck.append(building_deck.pop(0))
	return deck

# calls the build_deck function to build a playing deck
playing_deck = build_deck(decks)

print ""
print "Deck length:", len(playing_deck)
print ""

# deals cards to the player and dealer and returns the playing deck minus the dealt cards
def deal(deck):
	for i in range(0,2):
		player_hand.append(playing_deck.pop(random.randint(0 , len(playing_deck)-1)))
		dealer_hand.append(playing_deck.pop(random.randint(0 , len(playing_deck)-1)))
	return playing_deck, player_hand, dealer_hand

# takes a hand (list of cards) and separates the card from the suit, then returns the hand as a list of cards
def get_card_numbers(hand):
	cards = []
	for i in range(0, len(hand)):
		card = hand[i].split('-')
		cards.append(card[1])
	cards = sorted(cards)
	return cards

# adds the values of a hand's cards
def get_score(hand):
	score = 0
	ace_count = 0
	for i in range(0, len(hand)):
		if hand[i] == 'A':
			score += 11
			ace_count += 1
		elif hand[i] == 'J' or hand[i] == 'Q' or hand[i] == 'K':
			score += 10
		else:
			score += int(hand[i])
	return score

# returns the value of a hand
def check_score(hand):
	score = get_score(get_card_numbers(hand))
	return score

# deals a single card from the playing deck to the specified hand
def hit(hand):
	hand.append(playing_deck.pop(random.randint(0 , len(playing_deck)-1)))
	return playing_deck, hand

# pretty useless function, just prints the dealer wins
def dealer_wins():
	print "Dealer wins, better luck next time mate.\n"

# pretty useless function, just prints the player wins
def player_wins():
	print "You win mate! Ridgey didge, dinky die!\n"

# checks for a series of special cases and returns an appropriate response, if both hands are less than 5 cards and under 21 it evaluates the relative values
def compare(dealer_score, dealer_choice, player_score, player_choice):
	if player_choice == 'bust':
		print "Over 21, you bust!\n"
	elif dealer_choice == 'bust':
		print "Dealer bust, you win!\n"
	elif player_choice != 'five_under' and dealer_choice == 'five_under':
		print "Dealer got 5 cards under 21, dealer wins!"
	elif player_choice == 'five_under' and dealer_choice == 'five_under':
		print "You and the dealer both got 5 under 21, you lose."
	elif player_choice == 'five_under' and dealer_choice != 'five_under':
		print "You got five under 21, you win!"
	elif dealer_score >= player_score:
		dealer_wins()
	else:
		player_wins()

# runs the player's turn until bust or staying
def player_play(hand, deck): 
	card_count = 2
	choice = ''
	while choice != 'stay':
		score = check_score(hand)
		if score <= 21 and card_count == 5:
			choice = 'five_under'
			break
		elif score == 21:
			print "You have 21!"
			choice = 'stay'
		elif score <= 21:
			choice = raw_input(("You have been dealt %s cards and your score is %s, would you like to Hit or Stay? > " % (card_count, score))).lower()
			if choice == 'hit':
				deck, hand = hit(hand)
				card_count += 1
				print ""
				print "Deck length:", len(deck)
				print "\nYou got a %s.\n" % (hand[len(hand)-1])
				score = check_score(hand)
				if score > 21:
					choice = 'bust'
					break
					return deck
					return hand
			elif choice == 'stay':
				score = check_score(hand)
				print "\nYou are staying with %s and your hand is %s." %(score, hand)
	return hand, deck, choice

# runs the dealer's turn until bust or staying
def dealer_play(hand, deck): 
	card_count = 2
	choice = ''
	while choice != 'stay':
		score = check_score(hand)
		if score <= 21 and card_count == 5:
			choice = 'five_under'
			break
		elif score == 21:
			print "Dealer has 21!"
			choice = 'stay'
		elif score < 17:
			choice = 'hit'
			if choice == 'hit':
				deck, hand = hit(hand)
				card_count += 1
				print ""
				print "Deck length:", len(deck)
				print "\nDealer got a %s.\n" % (hand[len(hand)-1])
				score = check_score(hand)
				if score > 21:
					choice = 'bust'
					break
					return deck
					return hand
		elif score >= 17:
			choice = 'stay'
			score = check_score(hand)
			print "\nDealer is staying with %s and their hand is %s." %(score, hand)
	return hand, deck, choice

keep_playing = 'yes'	

# this while loop puts everything together and keeps running until the deck runs out or the 
# player says they don't want to play any more, I'm sure there's a more sophisticated way to do this.
while keep_playing == 'yes' and len(playing_deck) >= 10 :
	
	playing_deck, player_hand, dealer_hand = deal(playing_deck)
	
	print "Deck length:", len(playing_deck)
	print ""
	print "Your hand is: \n%s" % player_hand
	print ""
	print "You only get to see one of the dealers cards: \n['%s']" % dealer_hand[0]
	print ""
	
	dealer_score = check_score(dealer_hand)
	player_score = check_score(player_hand)
	
	player_hand, playing_deck, player_choice = player_play(player_hand, playing_deck)
	dealer_hand, playing_deck, dealer_choice = dealer_play(dealer_hand, playing_deck)
		
	player_score = check_score(player_hand)
	dealer_score = check_score(dealer_hand)
	
	print""
	print compare(dealer_score, dealer_choice, player_score, player_choice)
	print ""
	
	player_hand = []
	dealer_hand = []
	
	keep_playing = raw_input("Good hand! Would you like to try another? Type yes if you'd like to play again? > ")

print "\nThanks for playing! See you next time!\n"
