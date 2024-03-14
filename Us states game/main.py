import pandas
import turtle

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

img = "states.gif"
is_game_on = True

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(img)
turtle.shape(img)

def writing_on_map(state,x,y):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(x,y)
    new_turtle.write(state) 

def update_title(n):
    screen.title(f"{n}/50")    


while is_game_on:
    answer_state = screen.textinput(title="Guess the state ",prompt="What's another state name ?")

    if answer_state.title() == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states] #List Comprehension      
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")  
        break        
 
    if answer_state.title() in all_states:
        guessed_states.append(answer_state.title())
        answer_state_data = data[data.state == answer_state.title()]
        x_cor = int(answer_state_data.x)
        y_cor = int(answer_state_data.y)
        writing_on_map(answer_state.title(),x_cor,y_cor)   
        update_title(len(guessed_states))
    
    if len(guessed_states) >= 50:
        is_game_on = False    

