# Creating Maze BG
# 600 x 600 Screen Area
# 25 x 25 Grid
# Each sprite or block will be 24 x 24
# Coordinates
# TL: -288, 288
# TR: 288, 288
# BL: -288, -288
# BR: 288, -288

# PART 1: Setting up the maze
import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Escape 1051")
wn.setup(700, 700)
wn.tracer(0)

# Register shapes
images = ["rosen_right.gif", "rosen_left.gif",
          "cat.gif", "wall.gif",
          "snake_right.gif", "snake_left.gif"]
for image in images:
    turtle.register_shape(image)


# create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


# create player class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("rosen_right.gif")
        self.color("blue")
        self.penup()
        self.speed(0)

        # Player Characterisitcs
        self.gold = 0
        self.lives = 3

    def go_up(self):
        # Calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # Calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Calculate the spot to move to
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        self.shape("rosen_left.gif")

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # Calculate the spot to move to
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        self.shape("rosen_right.gif")

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    # Check if the player is hitting the chest
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 5:
            return True
        else:
            return False


# Creating the treasure
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("cat.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


def questions(treasure):
    questions={"What statment should be used when wanting to just display text? A)'print' B)'.format' C)'return'":"A",
               "What should you import when you want to use 'turtle' in your code? A)'Import turtle.Turtle' B)'Import turtle' C)'import random'":"B",
               "What does 'print('1+1')' output in python? A)'11' B)'2' C)'1+1'":"C",
               "What character should you use to comment out a piece of code? A)* B)* C)#":"C",
               "Which of the following cannot be used at the start of a variable name? A)An underscore B)A number C)An uppercase letter":"B",
               "Which of the following is the correct way to assign a numeric value to a variable? A)x=int(5) B) x=5 C)Both answers are correct":"C",
               "What is the index of 'b' in 'banana'? A)0 B)1 C)There is no index for strings":"A",
               "Which operator should be used when squaring a number? A)^ B)** C)%":"B",
               "What is the first the lesson in CS 1051? A) How to use turtle function B) Print 'Hello World!' C) How to use dictionaries": "B"}    
    for question in questions.keys():
        if question in asked_questions:
            continue
        print(question)
        answer = input("Enter:")
        answer = answer.upper()
        if answer == questions[question]:
            print("Correct!")
            asked_questions.add(question)
            return True
        else:
            print("Try Again!")
            break
    return False

print(questions)
# Creating the enemy
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("snake_left.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("snake_left.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("snake_right.gif")
        else:
            dx = 0
            dy = 0

        # Check if player is close
        # If so, go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        # Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            # choose a different direction
            # Choose different direction
            self.direction = random.choice(["up", "down", "left", "right"])

        # Set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Set to keep track of asked questions
asked_questions = set()
# Create levels list
levels = []
# Define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP         XXXXXX      XX",
    "X          XXXXXX      XX",
    "X  XXXXXX  XXXXXX  XXXXXX",
    "X  XXXXXX  XXXXXE  XXXXXX",
    "X  XXXXXX  XXXXX  XXXXXXX",
    "X     XXX               X",
    "XXXXX XXX              TX",
    "XXXXX      XXXXXXXXXXXX X",
    "XXX    XXXXXXXXXXXXXXXX X",
    "XXX            XXXXXXXX X",
    "XXX XXXXXXXXX  XXXXXXXX X",
    "X   XXXXX               X",
    "X XXXXXXX            XXXX",
    "X XXXXXXX XXXXXXXXXX XXXX",
    "X      E  XXXXX         X",
    "X         XXXXX         X",
    "XXXXX XXXXXXXXX XXXX  XXX",
    "XXXXX           XXXX  XXX",
    "XXXXX      T   XXXXX  XXX",
    "XXXXXXXXXXXXXX XXXXX  XXX",
    "XXXX                  XXX",
    "XXXX  XXXXXXXXXXXXXXXXXXX",
    "XXXX  XXXXXXXXXXXXXXXXXXX",
    "XXXX                    X",
    "XXXX                   TX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXXXXXXX     XXXX",
    "X    XXXXXXXX      XXXXXX",
    "XX     XXXX E    XXXXXXXX",
    "XXXX           XXXXXXXXXX",
    "XXXXX         XXXXXXXX  X",
    "X  XXXXXXX     XXXXX    X",
    "X     XXXXXXX   XX      X",
    "XX  T   XXXXXX      T XXX",
    "XXXXX      XXXX     XXXXX",
    "XXXXXXXX        XXXXXXXXX",
    "XXXXXXX           XXXXXXX",
    "XXXXXX     XX      XXXXXX",
    "XXXXX    XXXXXX  E XXXXXX",
    "XXXX     XXXXXX   XXXXXXX",
    "XXXXXX   XXX    XXXXXXXXX",
    "XXXXXXX        XXXXXXXXXX",
    "XXXXXXXXXXXXX    XXXXXXXX",
    "XXXXXXX   TXXX   XXXXX  X",
    "XXXXX     XXXXX    XX   X",
    "XXXX    XXXXXXXXX      XX",
    "XXX      XXXXX E   XXXXXX",
    "XXXXX     XX      XXXXXXX",
    "XXXXXX         XXXXXXXXXX",
    "XXXXXXXXXX        XXXXXXX",
    "XXXXXXXXXXXXX      XXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_3 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXX       XXXXXXX",
    "X   XXXXXX   XXX      XXX",
    "XX  XXXXX   XXXXXX     XX",
    "XX   XXX   XXXXXE  T X  X",
    "XX          XXX    XXX  X",
    "XXX                XXX  X",
    "XXX  XXXXX  XXXX   XX   X",
    "XXX  XXXXXX   XXX      XX",
    "XXX   XXXXXX E X   XXXXXX",
    "XXXX   XXXXXX     XXXXXXX",
    "XXXXX    XXXXXX    XXXXXX",
    "XXXX    XXXXXXXX    XXXXX",
    "XXX        XXXX     XXXXX",
    "X    XXXT          XXXXXX",
    "X   XXXXXX        XXXXXXX",
    "X   XXXX      XX    XXXXX",
    "X    X     XXXXXX     XXX",
    "XX  E   XXXXXXXXXXX    XX",
    "XXX       XXXXXXXXXX   XX",
    "XXXXXXX    XXXXXXX    XXX",
    "X  XXXXXX   XXXX   E XXXX",
    "X    XXXXX    X    XXXXXX",
    "XX    XXXX        XXXXXXX",
    "XXXX         XXX     XXXX",
    "XXXXXT     XXXXXXXX   XXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Add a treasure list
treasures = []

# Add enemies list
enemies = []

# Add maze to mazes list
levels.append(level_1)
levels.append(level_2)
levels.append(level_3)

def clear_chests(treasures):
    for treasure in treasures :
        treasure.destroy()
    treasures.clear()

def clear_enemies(enemies):
    for enemy in enemies:
        enemy.destroy()
    enemies.clear()

def clear_maze(level):
    walls.clear()
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the character at each x,y coordinate
            # NOTE the order of y and x in the next line
            character = level[y][x]
            # Calculate the screen
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X (represnting a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.clear()
    clear_chests(treasures)
    clear_enemies(enemies)

# Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the character at each x,y coordinate
            # NOTE the order of y and x in the next line
            character = level[y][x]
            # Calculate the screen
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X (represnting a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                # Add coordinates to wall list
                walls.append((screen_x, screen_y))

            # Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)

            # Check if it is a T (representing Treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            # Check if it is an E(representing Enemy)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

    for enemy in enemies:
        turtle.ontimer(enemy.move, t=250)


# Create class instances
pen = Pen()
player = Player()

# Create wall coordinate list
walls = []

# Set up the level
setup_maze(levels[0])

# Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

# Turn off screen updates
wn.tracer(0)

# Start moving enemies


# Create a variable to track the current level
current_level_index = 0

current_level_gold = 300

# Main Game Loop
while True:
    # Check for player collision with treasure
    # iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure) is True:
            # Add the treasure gold to the player gold when answer is correct
            if questions(treasure):
                player.gold += treasure.gold
                print("Player Gold: {}".format(player.gold))
                # Destroy the treasure
                treasure.destroy()
                # Remove the treasure from treasure list
                treasures.remove(treasure)
                break

    # Iterate through enemy list to see if the player collides
    for enemy in enemies:
        if player.is_collision(enemy):
            player.goto(-264, 264)
            player.lives -= 1
            print("Player dies!")
            print("Lives: {}".format(player.lives))
            if player.lives == -1:
                print("You lost! Try again later")
                turtle.bye()

    # Check if the player has enough gold to move to the next level
    if player.gold == current_level_gold:
        if player.gold == 900:
            print("Congradualations! You've won!")
            break
        clear_maze(levels[current_level_index])
        levels.remove(levels[current_level_index])
        setup_maze(levels[current_level_index])
        current_level_gold += 300
        player.lives += 1
        player.goto(-264, 264)
    
        
    # Update screen
    wn.update()
