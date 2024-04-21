#Creating Maze BG

    #600 x 600 Screen Area
    # 25 x 25 Grid
    # Each sprite or block will be 24 x 24

    #Coordinates
        #TL: -288, 288
        #TR: 288, 288
        #BL: -288, -288
        #BR: 288, -288
    
#PART 1: Setting up the maze 
import turtle

wn = turtle.Screen()
wn.bgcolor("LightSteelBlue")
wn.title("Escape 1051")
wn.setup(700,700)

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
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

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

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)



#Create levels list
levels = [""]

#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP         XXXXXXXXXXXXXX",
"X XXXXXXXX XXXXXXX     XX",
"X XXXXXXXX XXXXXXX XXXXXX",
"X XXXXXXXX XXXXXXX XXXXXX",
"X XXXXXXXX XXXXXXX XXXXXX",
"X     XXXX XXXXXXX XXXXXX",
"XXXXX XXX               X",
"XXXXX XXX XXXXXXXXXXXXX X",
"XXX            XXXXXXXX X",
"XXX XXXXXXXXXX XXXXXXXX X",
"XXX XXXXXXXXXX XXXXXXXX X",
"X   XXXXX               X",
"X XXXXXXX XXXXXXXXXX XXXX",
"X XXXXXXX XXXXXXXXXX XXXX",
"X         XXXXX         X",
"XXXXX XXXXXXXXX XXXX XXXX",
"XXXXX XXXXXXXXX XXXX XXXX",
"XXXXX           XXXX XXXX",
"XXXXXXXXXXXXXX XXXXX XXXX",
"XXXXXXXXXXXXXX XXXXX XXXX",
"XXXX           XX    XXXX",
"XXXX  XXXXXXXXXXXXXXXXXXX",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

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
                pen.stamp()
                #Add coordinates to wall list
                walls.append((screen_x, screen_y))

            #Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)
        


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

#Main Game Loop
while True:
    #Update screen
    wn.update()









