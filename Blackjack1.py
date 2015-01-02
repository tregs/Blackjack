import random

complete_deck = [
'S-2', 'S-3', 'S-4', 'S-5', 'S-6', 'S-7', 'S-8', 'S-9', 'S-10', 'S-J', 'S-10', 'S-J', 'S-Q', 'S-K', 'S-A',
'C-2', 'C-3', 'C-4', 'C-5', 'C-6', 'C-7', 'C-8', 'C-9', 'C-10', 'C-J', 'C-10', 'C-J', 'C-Q', 'C-K', 'C-A',
'D-2', 'D-3', 'D-4', 'D-5', 'D-6', 'D-7', 'D-8', 'D-9', 'D-10', 'D-J', 'D-10', 'D-J', 'D-Q', 'D-K', 'D-A',
'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'H-7', 'H-8', 'H-9', 'H-10', 'H-J', 'H-10', 'H-J', 'H-Q', 'H-K', 'H-A'
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
print playing_deck
print ""

# deals cards to the player and dealer and returns the playing deck minus the dealt cards
def deal(deck):
	for i in range(0,2):
		player_hand.append(playing_deck.pop(random.randint(0 , len(playing_deck)-1)))
		dealer_hand.append(playing_deck.pop(random.randint(0 , len(playing_deck)-1)))
	return playing_deck, player_hand, dealer_hand

playing_deck, player_hand, dealer_hand = deal(playing_deck)

print "Player hand: %s" %player_hand
print "Dealer hand: %s" %dealer_hand[0]
print ""

# takes a hand (list of cards) and separates the card from the suit, then returns the hand as a list of cards
def get_card_numbers(hand):
	cards = []
	for i in range(0, len(hand)):
		card = hand[i].split('-')
		cards.append(card[1])
	cards = sorted(cards)
	return cards

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

def check_score(hand):
	score = get_score(get_card_numbers(hand))
	return score

dealer_score = check_score(dealer_hand)
player_score = check_score(player_hand)

def hit(hand):
	hand.append(playing_deck.pop(random.randint(0 , len(playing_deck)-1)))
	return playing_deck, hand

def dealer_wins():
	print "Dealer wins, better luck next time mate."

def player_wins():
	print "You win matey! Ridgey didge, dinky die!"

def compare(score1, score2):
	if dealer_score >= player_score:
		dealer_wins()
	else:
		player_wins()

print compare(dealer_score, player_score)

def play(): 
	player_card_count = 2
	dealer_card_count = 2
	while player_choice != 'stay':
		player_score = check_score(player_hand)
		if player_score <= 21 and player_card_count == 5:
			print "You have five under 21!
			player_choice = 'stay'
		elif player_score == 21:
			choice = 'stay'
		elif player_score <= 21:
			choice = raw_input(("You have been dealt %s cards and your score is %s, would you like to Hit or Stay? > " % (player_card_count, player_score)).lower())
			playing_deck, player_hand = hit(player_hand)
			return playing_deck
			return player_hand
		if player_choice = 'stay'
			print "You are staying with %s." %player_score
		else
	return dealer_choice, player_choice, playing_deck
	
	'''while player_choice != 'stay':
		dealer_score = check_score(dealer_hand)
		player_score = check_score(player_hand)
		if dealer_score > 21:
			player_wins()
			break
		elif dealer_score < 17:
			playing_deck, dealer_hand = hit(dealer_hand)
			dealer_card_count += 1
			return playing_deck
			return dealer_hand
		else:
			dealer_choice = 'stay'
			print "The dealer has chosen to stay."
		if player_score <= 21 and player_card_count == 5:
			player_choice = 'stay'
		elif player_score == 21:
			choice = 'stay'
		elif player_score <= 21:
			choice = raw_input(("You have been dealt %s cards and your score is %s, would you like to Hit or Stay? > " % (player_card_count, player_score)).lower())
			playing_deck, player_hand = hit(player_hand)
			return playing_deck
			return player_hand
		if player_choice = 'stay'
			print "You are staying with %s." %player_score
		else
	return dealer_choice, player_choice, playing_deck'''
		

def next_move(score):
	iif choice == 'hit':
			playing_deck, player_hand = hit(player_hand)
			return playing_deck
			return player_hand
		elif choice == 'stay':
			return choice
	elif player_score > 21:
		choice = "Bust"
	else:
		print "Something went wrong in the hit_or_stay function."
	return choice


'''


