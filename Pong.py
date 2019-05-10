import turtle
import os
import math


#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Pong")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Creating player 1
player1 = turtle.Turtle()
player1.color("white")
player1.shape("square")
player1.shapesize(stretch_wid = 5, stretch_len= .5 )
player1.penup()
player1.speed(0)
player1.setposition(-380,0)

#Creating player 2
player2 = turtle.Turtle()
player2.color("white")
player2.shape("square")
player2.shapesize(stretch_wid = 5, stretch_len= .5 )
player2.penup()
player2.speed(0)
player2.setposition(380,0)

#Creating the ball
ball = turtle.Turtle()
ball.color("white")
ball.shape("square")
ball.shapesize(stretch_wid = .5, stretch_len = .5)
ball.penup()
ball.speed(0)
ball.setposition(0,0)

ballx = .3
bally = .3

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0      Player B: 0", align="center", font=("Courier",24,"normal"))

#Functions
def player1_up():
    y = player1.ycor()
    y += 30
    player1.sety(y)
    if player1.ycor() > 250:
        player1.sety(250)

def player1_down():
    y = player1.ycor()
    y -= 30
    player1.sety(y)
    if player1.ycor() < -250:
        player1.sety(-250)

def player2_up():
    y = player2.ycor()
    y += 30
    player2.sety(y)
    if player2.ycor() > 250:
        player2.sety(250)

def player2_down():
    y = player2.ycor()
    y -= 30
    player2.sety(y)
    if player2.ycor() < -250:
        player2.sety(-250)

#Keybinds
wn.listen()
wn.onkey(player1_up,"w")
wn.onkey(player1_down,"s")
wn.onkey(player2_up,"Up")
wn.onkey(player2_down,"Down")


#Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ballx)
    ball.sety(ball.ycor() + bally)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        bally *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        bally *= -1

    if ball.xcor() > 390:
        ball.setposition(0,0)
        ballx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.setposition(0,0)
        ballx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    #Paddle and Ball Collisions
    if (ball.xcor() > 370 and ball.xcor() < 375) and (ball.ycor() < player2.ycor() + 50 and ball.ycor() > player2.ycor() - 50):
        ball.setx(370)
        ballx *=-1

    if (ball.xcor() < -370 and ball.xcor() > -375) and (ball.ycor() < player1.ycor() + 50 and ball.ycor() > player1.ycor() - 50):
        ball.setx(-370)
        ballx *=-1

    #Win Conditions

    if score_a == 5:
        player1.hideturtle()
        player2.hideturtle()
        ball.hideturtle()
        player1_win = turtle.Turtle()
        player1_win.speed(0)
        player1_win.color("white")
        player1_win.penup()
        player1_win.setposition(0, 0)
        player1_win_string = "Player 1 Wins"
        player1_win.write(player1_win_string, False, align="center", font=("Courier", 28, "bold"))

        print("Player 1 Wins")


    if score_b == 5:
        player1.hideturtle()
        player2.hideturtle()
        ball.hideturtle()
        player2_win = turtle.Turtle()
        player2_win.speed(0)
        player2_win.color("white")
        player2_win.penup()
        player2_win.setposition(0,0)
        player2_win_string = "Player 2 Wins"
        player2_win.write(player2_win_string, False, align="center", font=("Courier", 28, "bold"))

        print("Player 2 Wins")

