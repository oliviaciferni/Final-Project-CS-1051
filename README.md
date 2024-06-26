# Hello! This is a video walk through for our game “Escape 1051” solely created in Python for CIS 1051’s Final Project. https://youtu.be/a0J3bdVyAd8?si=0Y7gPWhLwCd5XSAh.

My name is Sheila Jimenez, I’m a sophomore, and I created this game with Olivia Ciferni, who’s a freshman. 

Our game, Escape 1051, is a maze game. The player begins with 3 lives, and 0 gold. There are three cats in each level which will ask a different question about python. You must answer each question about python correctly in order to collect all the gold from the cats. Each cat holds 100 gold totalling to 300 in a level. Once you reach a total of 900 gold, and pass 3 levels you win!
However, Escaping 1051 is not going to be easy, as there are snakes that will increase through each level.  Once you hit a snake you are taken back to the start and lose a life. You can gain 1 life once you complete each level.

# We were able to follow an intermediate python maze tutorial on youtube, and use functions and modules learned in class like, file read, list, def, if, and while statements to create a fully functioning maze game, with sprites in python 3.12.1.  

 During the making of this game, we were able to learn and incorporate many pythons built in modules. In this video I’m going to go over our use of ‘‘class and initialize(self)”,  “onkey”, and “ontimer”, since these are a large part of making the code work and are newer modules to us.

“Class” is not an object but can define an object. “Creating a new class creates a new type of object, allowing new instances of that type to be made.” For instance, our class "Pen" is a child of turtle modules turtle class. Our "Pen" is our turtle. Anything our "Pen" can do, our turtle can do. 

When creating a class we need to use the method initialize, the  "__init__" followed with (self). The method takes the object as its first argument (self), followed by any additional arguments that need to be passed to it. "self" refers to the object that we are calling. Because Pen is the child of a turtle class we have to initialize that class too! This is why we have " turtle.Turtle.__init__(self)” under __init__(self), and this under class pen(turtle.Turtle). While setting up the rest of the code using our class Pen, for every instance that we create it's going to be a square, white, with no trail because of "penup()”, and a speed of (0). 

Our class pen became incredibly important in setting up our maze,
The "Setup_maze" definition calls each level that was created and appended to the “levels” list.
“for y in range length of level” starts with our first row of X in our first “level_1”. Each row of X, is separated by commas and the spaces, which have no condition create a pathway for our sprite, enemies and chests. Then the nested loop “for x in range of the length of level[y] looks at the length of the row, reading each X in each row of X’s. Since each block is 288 pixels, which was already created in python from changing the shape to “square”, we must increase by X times 24 to go to the next block. This translates our screen to x and y.

Which then allows us to create variables for our game components. For instance, “if character == “X”. The turtle will go to this, screen_x and screen_y coordinate, give the pen shape “wall.gif”, stamp, and then add these coordinates to the walls list. The for loop will continue to look for each variable and change each character for each level. Here is where we call and place our player, “P’”  created in the player definition. It also applies to the treasure “T” aka cats, and enemies “E”. Which each have their own definition and parameters at the top as well. 

Once the Map was set up, and each character was successfully placed on the map we were able to create moving sprites that can follow you around the map.
The "turtle.ontimer method" install a timer, which calls fun after t milliseconds. In this for loop, “for enemy in enemies” our enemies call the defintion “move” to move to a  random x, and y coordinate interval from 100 to 300 milliseconds!Normally it can only be set once, but since we placed the for loop in our setup_maze function, for each level, each enemy will randomly move. 
Move is in the class Enemy, it uses the function direction to face, “up, down, left, and right”, and delta x and y to move “up, down, left and right” 24 pixels in any direction. 
It also is where we also placed the if statements  and definitions of having the sprite check is the player is close and calculate the spot to move to 
Here is_close is called, it is called if the distance is 75 pixels, it calculates the player and other characters distance. Move finally calls this to the object, in this case enemies.

# There became difficulties during the transition from level to level in this game. As you can see we have created level_1, 2 and 3. 
In order to call each level we have written setup_maze(). This is called in our Main Game Loop, when the player reaches each target gold amount in each level. I started with simply writing, levels.remove(levels[current_level_index] setup_maze(levels[current_level_index]). The Current_level_index equaled 0. While I wished this would delete the previous level and move on to the next level without any issues, it presented our biggest one. While the level would move on to the next, all of the previous information, walls, enemies, and chests were not deleted. It then became clear we had to write definitions new to clear the walls, chests and enemies when called in our Main Game Loop in order to successfully move to the next level. 

I was able to copy and paste the variables that drew the walls, and enemies, and essentially do the opposite.  For the walls we used pen.clear(), and  the destroy() definition for the enemies and treasures, to officially create a blank slate. 

This destroy definition is in Class Treasure and Enemies, as when you answer the question correctly, the Cat/Treasure is hidden and moves off screen. “destroy()” did not work very easily since it allowed the chest to still exist. So, it was decided to .clear() is like the walls, since all of these characters were created with our Class.Pen() which is a child of the turtle module. 

# It was easy to enjoy customizing our map, player, enemies, and chest. 
Since it was only a matter of reading the files we downloaded and called them in the code and for each character. 
As you can see, it is Professor Rosen, he is avoiding the python snakes, answering each python question and collecting the gold from his cat in order to Escape 1051!.
After we were able to bind “setp_upmaze” to each x and y pixel and get the transition to each level to work we also enjoyed simply typing an X to correspond to a wall. 
This made creating our own map incredibly easy. The same goes for each enemy and treasure as we were able to place them anywhere we chose. It truly became our game because of this.
