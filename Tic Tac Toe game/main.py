import random

board = list(range(1,10))
COMBINATIONS = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
us_inps = []
cp_inps = []

print("-----WELCOME TO TIC TAC TOE GAME-----")

def print_board(board):
    print("-" * 13)
    for i in range(len(board)):
        if (i+1)%3 != 0:
            print(board[i], end = " | ")
        else:
            print(f"{board[i]}")
            print("-"*13)

def check_winner_for_user(us_inps):
    for combination in COMBINATIONS:
        if all(element in us_inps for element in combination):
            return True  # Combination found, exit the loop
    return False # No combination found


def check_winner_for_comp(cp_inps):
    for combination in COMBINATIONS:
        if all(element in cp_inps for element in combination):
            return True  # Combination found, exit the loop
    return False  # No combination found

is_game_on = True

while is_game_on:
    print_board(board)
    user_inpt = int(input("Enter a number where you want to X in that square: "))
    board[user_inpt - 1] = "X"
    us_inps.append(user_inpt)
    print_board(board)
    if check_winner_for_user(us_inps):
        print("You Win!")
        is_game_on = False
    else:
        numbers = [x for x in board if not isinstance(x, str)]  # Filter out strings
        if numbers != []:
            print("Its computer's turn")
            comp_inpt = random.choice(numbers)
            board[comp_inpt - 1] = "O"
            cp_inps.append(comp_inpt)
            if check_winner_for_comp(cp_inps):
                print_board(board)
                print("The Computer Won")
                is_game_on = False
        else:
            print("Its a Draw!! \n GAME OVER")
            is_game_on = False    


        