import turtle

wn = turtle.Screen()
wn.bgcolor("LightSteelBlue")
wn.title("Escape 1051")
wn.setup(700,700)

#The pen for the blocks!
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

#Add maze to maze list
levels.append(level_1)

#Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range (len(level[y])):
            #get the character at each x,y coordinate
            #note the order of y and x in the next line
            character = level[y][x]
            #calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #check if it is an X (representing a wall)
            if character =="X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

            #Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)

#Create class instances
pen = Pen()
player = Player()

#Setting the level
setup_maze(levels[1])

#Main Game Loop
while True:
    pass

