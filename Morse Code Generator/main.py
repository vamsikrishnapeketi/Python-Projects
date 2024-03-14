from data import morse_code

print("WELCOME TO MORSE CODE TRANSLATOR")
is_cont = True

while is_cont:
    user_choice = input("Do you want to convert the sentence into morse code.If yes type y else type n: ")
    if user_choice == 'y':
        user_input = input("Enter the text here that you want to convert to its equivalent morse code.: \n").upper() 
        morse_ouput = ""
        for letter in user_input:
            if morse_ouput == "":
                morse_ouput = morse_code[letter] 
            elif letter == " ":
                continue       
            else:
                morse_ouput = morse_ouput + " " + morse_code[letter]

        print(f"The morse code is \n {morse_ouput}")
    else:
        is_cont = False

print("See ya! Bye")