import turtle
import pandas

data = pandas.read_csv('50_states.csv')
screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f'{len(guessed_states)}/50', 'Guess a new state:').title()
    all_states = data.state.to_list()

    if answer_state == 'End':
        new_data = pandas.DataFrame(all_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_cord = data[data.state == answer_state]
        t.goto(int(state_cord.x), int(state_cord.y))
        t.write(f'{answer_state}')
        all_states.remove(answer_state)
        guessed_states.append(answer_state)