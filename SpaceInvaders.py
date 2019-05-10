import turtle
import os
import math
import random

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("/home/aaron/PycharmProjects/SpaceInvaders2.7/Images/space_invaders_background.gif")
wn.setup(width=700, height=700)
wn.register_shape("/home/aaron/PycharmProjects/SpaceInvaders2.7/Images/invader.gif")
wn.register_shape("/home/aaron/PycharmProjects/SpaceInvaders2.7/Images/player.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial",14,"normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("/home/aaron/PycharmProjects/SpaceInvaders2.7/Images/player.gif")
player.penup()
player.speed(0)
player.setposition(0,-270)
player.setheading(90)

playerspeed = 15

#Choose a number of enemies
number_of_enemies = 5
#Create an Empty list
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())


for enemy in enemies:
    enemy.color("red")
    enemy.shape("/home/aaron/PycharmProjects/SpaceInvaders2.7/Images/invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x, y)

enemyspeed = 1

#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)



#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 10

#Define bullet state
#ready - ready to fire
#fire - bullet is firing

bulletstate = "ready"

def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"

        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 18:
        return True
    else:
        return False

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main Game Loop
while True:
    wn.tracer(2)

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor()> 280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        if enemy.xcor()<-280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        #Check if enemy reaches bottom
        if enemy.ycor()<-270:
            for e in enemies:
                e.hideturtle()

            player.hideturtle()

            gameover_pen = turtle.Turtle()
            gameover_pen.speed(0)
            gameover_pen.color("white")
            gameover_pen.penup()
            gameover_pen.setposition(0, 0)
            gameoverstring = "Game Over!"
            gameover_pen.write(gameoverstring, False, align="center", font=("Arial", 28, "bold"))
            gameover_pen.hideturtle()


            print ("Game Over")
            break


        # Check for a collision between the bullet and the enemy
        if bulletstate == "fire":
            if isCollision(bullet, enemy):
                # Reset the bullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0, -400)
                # Reset the enemy
                enemy.setposition(-200, 270)
                #Add points to score
                score += 10
                scorestring = "Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        # Check for a collision between the enemy and player
        if isCollision(player, enemy):
            player.hideturtle()
            for e in enemies:
                e.hideturtle()
            print ("Game Over")
            break

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has gone to the top
    if bullet.ycor()> 280:
        bullet.hideturtle()
        bulletstate = "ready"

turtle.mainloop()