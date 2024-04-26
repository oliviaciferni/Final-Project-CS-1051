#Creating Maze BG
    #600 x 600 Screen Area
    # 25 x 25 Grid
    # Each sprite or block will be 24 x 24
    #Coordinates
        #TL: -288, 288
        #TR: 288, 288
        #BL: -288, -288
        #BR: 288, -288
    
import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Escape 1051")
wn.setup(700,700)
wn.tracer(0)

#Register shapes
images = ["snake_left.gif","snake_right.gif","rosen_right.gif","rosen_left.gif","cat.gif","wall.gif"]
for image in images:
          turtle.register_shape(image)

#create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
#create player class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("rosen_right.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0
        
    def go_up(self):
        #Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        
        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_down(self):
        #Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_left(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        self.shape("rosen_left.gif")
         
        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_right(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        self.shape("rosen_right.gif")
        
        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    #Check if the player is hitting the chest
    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2)+(b ** 2))
        
        if distance < 5:
            return True
        else:
            return False
        
#Creating the treature
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

        #Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #choose a different direction
            self.direction = random.choice(["up", "down", "left", "right"])

        #Set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100,300))

                                                  
def questions(treasure):
    questions={"What statment should be used when wanting to just display text? A)'print' B)'.format' C)'return'":"A",
            "What should you import when you want to use 'turtle' in your code? A)'Import turtle.Turtle' B)'Import turtle' C)'import random'":"B"}
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

#Set to keep track of asked questions
asked_questions = set()

#Create levels list
levels = [""]

#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP         XXXXXXXXXXXXXX",
"X XXXXXXXX XXXXXXX     XX",
"X XXXXXXXX XXXXXXX XXXXXX",
"X XXXXXXXX XXXXXXX XXXXXX",
"X XXXXXXXX XXXXXXXEXXXXXX",
"X     XXXX XXXXXXX XXXXXX",
"XXXXX XXX              TX",
"XXXXX XXX XXXXXXXXXXXXX X",
"XXXE           XXXXXXXX X",
"XXX XXXXXXXXXX XXXXXXXX X",
"XXX XXXXXXXXXX XXXXXXXX X",
"X   XXXXX               X",
"X XXXXXXX XXXXXXXXXX XXXX",
"X XXXXXXX XXXXXXXXXX XXXX",
"X      E  XXXXX         X",
"XXXXX XXXXXXXXX XXXX XXXX",
"XXXXX XXXXXXXXX XXXX XXXX",
"XXXXX       T   XXXX XXXX",
"XXXXXXXXXXXXXX XXXXX XXXX",
"XXXXXXXXXXXXXX XXXXX XXXX",
"XXXX           E    XXXX",
"XXXX  XXXXXXXXXXXXXXXXXXX",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]
#Add a treasure list
treasures = []

#Add enemies list
enemies = []

#Add maze
levels.append(level_1)

#Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x,y coordinate
            #NOTE the order of y and x in the next line
            character = level[y][x]
            #Calculate the screen
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            #Check if it is an X (represnting a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                #Add coordinates to wall list
                walls.append((screen_x, screen_y))
                
            #Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)
                
            #Check if it is a T (representing Treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            #Check if it is an E (representing Enemy)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))
                
#Create class instances
pen = Pen()
player = Player()

#Create wall coordinate list
walls = []

#Set up the level
setup_maze(levels[1])

#Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

#Turn off screen updates
wn.tracer(0)

#Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)
    
#Main Game Loop
while True:
    #Check for player collision with treature
    #iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure) is True:
            #Add the treasure gold to the player gold when answer is correct
            if questions(treasure):
                player.gold += treasure.gold
                print("Player Gold: {}".format(player.gold))
                #Destroy the treasure
                treasure.destroy()
                #Remove the treasure from treasure list
                treasures.remove(treasure)
                break
            
    #Iterate through enemy list to see if the player collides
    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player dies!")
    #Update screen
    wn.update()
