import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)

#Register shapes

#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Treasure(turtle.Turtle):
    def __init__(self, x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
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
            self.goto(self.xcor(), self.ycor() + 24)

    def go_down(self):
        # Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(self.xcor(), self.ycor() - 24)

    def go_left(self):
        # Calculate the spot to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
          self.goto(self.xcor() - 24, self.ycor())

    def go_right(self):
        # Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(self.xcor() + 24, self.ycor())

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction = random.choice(["up","down","left","right"])

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

        elif self.direction == "right":
            dx = 24
            dy = 0

        else:
            dx = 0
            dy = 0

        #Check if player is close
        #If so, go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        #Calculate the spot to move on
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #Choose a different direction
            self.direction = random.choice (["up","down","left","right"])

        #Set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100,300))

    def is_close(self,other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()



#Create Level List
levels = [""]

#Define First Level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXX     EXXXE      TX",
"X   XXX      XXX        X",
"X   XXX      XXX        X",
"X                       X",
"XXXXXXXXXXXXX  XXX  XXXXX",
"XXXXXXXXXXXXX  XXX  XXXXX",
"XXXXXXXXXXXXX  XXX  XXXXX",
"X    XXXE               X",
"X    XXX                X",
"X    XXXXXX     XXXX    X",
"XE   XXXXXX E   XXXX   EX",
"X    XXXXXX     XXXX    X",
"X               XXXX    X",
"X               XXXX    X",
"X    XXX   XX   XXXX    X",
"X    XXX   XX   XXXX    X",
"X    XXX                X",
"X                       X",
"X    XXXXXXXXX    XXXXXXX",
"X    XXXXXXXXX    XXXXXXX",
"X    XXXXXXXXX    XXXXXXX",
"X     EXXX              X",
"XT     XXX  E          TX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",

]

#Add a treasures list
treasures = []

#Add an enemies list
enemies = []

#Add Maze to Mazes List
levels.append(level_1)

#Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x,y coordinate
            #NOTE the order of y and x in the next line
            character = level[y][x]
            #Calculate if it is an X (representing a wall)
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                #Add coordinates to wall list
                walls.append((screen_x, screen_y))

            #Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)

            #Check if it is a T (representing a treasure)
            if character == "T":
                treasures.append(Treasure(screen_x,screen_y))

            #Check if it is an E (representing an enemy)
            if character == "E":
                enemies.append(Enemy(screen_x,screen_y))


#Create Class Instances
pen = Pen()
player = Player()

#Create wall coordinate list
walls = []

#Set up the level
setup_maze(levels[1])

#Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

#Turn off screen up dates
wn.tracer(0)

#Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

#Main Game Loop
while True:
    #Check for player collision with treasure
    #Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            #Add the treasure gold to the player gold
            player.gold += treasure.gold
            print ("Player Gold: {}".format(player.gold))
            #Destroy the treasure
            treasure.destroy()
            #Remove the treasure from the treasures list
            treasures.remove(treasure)

    #Iterate through enemy list to see if the player collided
    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player dies!")
            player.hideturtle()
            for enemy in enemies:
                enemy.hideturtle()
            lose_pen = turtle.Turtle()
            lose_pen.speed(0)
            lose_pen.color("red")
            lose_pen.penup()
            lose_pen.setposition(0,0)
            lose_pen_string ="Player died!"
            lose_pen.write(lose_pen_string, False, align = "center", font=("Papyrus", 28, "bold"))
            break

    if player.gold == 300:
        print("Player Wins")
        player.hideturtle()
        for enemy in enemies:
            enemy.hideturtle()
        win_pen = turtle.Turtle()
        win_pen.speed(0)
        win_pen.color("gold")
        win_pen.penup()
        win_pen.setposition(0, 0)
        win_pen_string = "Player Wins!"
        win_pen.write(win_pen_string, False, align="center", font=("Papyrus", 28, "bold"))
        


    #Update Screen
    wn.update()