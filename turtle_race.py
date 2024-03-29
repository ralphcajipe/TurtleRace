import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
# turtle colors
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black',
          'brown', 'pink', 'cyan']


def get_number_of_racers():
    # racers = 0
    while True:
        t_racers = input('Enter number of turtle racers (2 - 10): ')
        if t_racers.isdigit():
            t_racers = int(t_racers)
        else:
            print('Input is not numeric... Try Again!')
            continue

        if 2 <= t_racers <= 10:
            return t_racers
        else:
            print('Number not in range[2-10]... Try Again!')


def race(t_colors):
    turtles = create_turtles(t_colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return t_colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Race!')


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the", winner, "turtle! ＼(^o^)／")
time.sleep(2)
