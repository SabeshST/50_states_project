import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
missed_states = data.state.to_list()
my_turtle = turtle.Turtle()

screen = turtle.Screen()
screen.screensize(500,500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


game_on = True
correct_count = 0
guess_list = []

while len(guess_list) < 50 and game_on:
    guess = turtle.textinput(f"{correct_count}/50 Guessed Correctly",
                             "Enter state name below:").title()
    if guess in all_states and guess not in guess_list:
        guess_list.append(guess)
        missed_states.remove(guess)
        correct_count += 1

        state = data[data.state == guess]
        my_turtle.hideturtle()
        my_turtle.teleport(state.x.item(), state.y.item())
        my_turtle.write(state.state.item())

    else:
        play_again = turtle.textinput("Play again?", "Would you like to play again: y/n")
        if play_again == "n":
            missed_states_data = pandas.DataFrame(data=missed_states)
            missed_states_data.to_csv("missed_states.csv")
            print(f"You guessed {correct_count}/50 right!")
            game_on = False
            screen.bye()

        elif play_again == "y":
            correct_count = 0
            guess_list = []
            my_turtle.clear()


# screen.exitonclick()