from art import logo
import random

choice = input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ")
if (choice == 'y'):
    cont_game = True
else:
    cont_game = False

game_ends = False    
user_cards = []
computer_cards = []

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return (random.choice(cards))

def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def compare(computer_score,user_score): #compare(computer_score,user_score)
    if computer_score == user_score:
        print("Its a Draw")
    elif computer_score == 0:
        print("The Computer Wins")
    elif user_score == 0:
        print("You Win!!")
    elif computer_score > 21:
        print("You win")
    elif user_score > 21:
        print("The Computer wins")
    elif computer_score > user_score:
        print("The Computer wins")
    else:
        print("You win")


while cont_game:
    print(logo)
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    while not game_ends:
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if(user_score > 21 or user_score == 0 or computer_score == 0):
            game_ends = True
        else:
            take_card_choice = input("Type 'y' to get another card,type n to pass: ")   
            if(take_card_choice == 'y'):
                user_cards.append(deal_card())
            else:
                game_ends = True
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    compare(computer_score,user_score)
    cont_choice = input("Do you want to play again ? Type 'y' or 'n' ")
    if cont_choice == 'y':
        cont_game = True
        game_ends = False
        user_cards = []
        computer_cards = []
    else:
        cont_game = False    

