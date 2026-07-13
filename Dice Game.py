# Dice Game.py

"""This is a self-knowledge test module for how to make a dice game using 
turtle graphics.
Before I only did this once to create a Tic-Tac-Toe game with a source code from https://pastebin.com/XqdBMNhR,made by a user named pythonplaygroound. 
I am relatively new to python with a little over 6 months of studies under my belt. 
This is just another go at making a worthwhile project to build my experience on this platform and hopefully learn more!"""

from os import remove
import turtle
import random 

# Structuring the screen

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("The Dice Game")
screen.bgcolor("#006400")                                                                       # Emerald green background for a classy look
screen.tracer(0)

# The screen tracer will turn off initial animations for an instant outline

# Moving on to creating the drawing

t = turtle.Turtle()
t.hideturtle()
t.speed(5)

# Defining the relative coordinates for the 7 possible dot posiitions 
# based on the 3x3 rule of a dice

DOT_POSITIONS = {
    "center": (0, 0),
    "top_left": (-150, 150),
    "top_right": (150, 150),
    "bottom_left": (-150, -150),
    "bottom_right": (150, -150),
    "middle_left": (-150, 0),
    "middle_right": (150, 0)
}

# Mapping out roll numbers (1-6) to their positions on the dice face
DICE_FACE = {
    1: ["center"],
    2: ["top_left", "bottom_right"],
    3: ["top_left", "center", "bottom_right"],
    4: ["top_left", "top_right", "bottom_left", "bottom_right"],
    5: ["top_left", "top_right", "center", "bottom_left", "bottom_right"],
    6: ["top_left", "top_right", "middle_left", "middle_right", "bottom_left", "bottom_right"]
}

def draw_dot():
    """Draws a single dot at the current turtle position."""
    t.clear()
    t.penup()
    t.goto(-500, 500)                                                                             # Move to the top-left corner of the dice face
    t.pendown()
    t.color("#D3AF37")                                                                          # Gold color for the dot, because why not? :)
    t.begin_fill()
    for _ in range(4):
        t.forward(200)
        t.right(130)
    t.end_fill()

def draw_dots(roll_value):
    """Draws the dots on the dice face based on the roll value."""
    t.color("#D3AF37")                                                                        # Gold again!
    needed_dots = DICE_FACE[roll_value]
    t.clear()                                                                                   # Erases the previous dice dots!

    for position in needed_dots:
        x, y = DOT_POSITIONS[position]
        t.penup()
        t.goto(x, y - 30)                                                                       # Adjusting for the dot's radius
        t.pendown()
        t.begin_fill()
        t.circle(30)                                                                            # Draw a dot with radius 30
        t.end_fill()

def roll_dice():
    """Rolls the dice and updates the drawing."""
    roll_value = random.choice([1, 2, 3, 4, 5, 6])                                              # Generates the random number between 1 and 6
    draw_dots(roll_value)
    screen.update()                                                                             # Update the screen to show the new roll

# Adding Keyboard bindings for rolling the dice

screen.listen()
screen.onkey(roll_dice, "space")                                                                # Press space to roll the dice

# Starting Instructions

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.color("#030001")
text_turtle.penup()
text_turtle.goto(0, -400)                                                                       # Positioning the text below the dice face
text_turtle.write("Press SPACE to roll the dice!", align="center", font=("Times New Roman", 24, "bold"))



# Drawing the intial face on startup

roll_dice()

# Keep the window open until the user closes it

screen.mainloop()