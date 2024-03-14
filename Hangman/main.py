import random as r
from hangman_words import word_list
from hangman_art import stages,logo

end_of_game = False
display = []
lives = 6
print(logo)
chosen_word = r.choice(word_list)
for i in chosen_word:
    display.append("_")
print(display)
while not end_of_game:
    guess = input("Guess a letter\n").lower()
    for i in range(len(chosen_word)):      
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]       
    if guess not in chosen_word :
        lives -= 1   
        print(stages[lives])     
    print(display)        
    if "_" not in display:
        end_of_game = True
        print("You win")
    if lives == 0:
        end_of_game = True
        print("You lose")    
print(f"The word is {chosen_word}")

