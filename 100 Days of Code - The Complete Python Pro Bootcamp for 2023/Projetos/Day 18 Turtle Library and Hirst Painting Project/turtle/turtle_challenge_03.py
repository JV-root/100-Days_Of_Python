# The challenge is to draw an spriograph using the turtle library.

import turtle as t
import random

tim = t.Turtle()

t.colormode(255)


def random_color():
    """Generate a random color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

tim.speed("fastest")


def draw_spirograph(size_of_gap):
    """Draw a spirograph."""
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

