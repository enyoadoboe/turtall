import turtle
import random
import math
from turtle import *

TurtleScreen._RUNNING = True

#create animation
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Objects Simulator")

#create player
player = turtle.Turtle()
player.shape("turtle")
player.shapesize(2, 2, 5)
player.color("dark cyan")
player.up()
player.speed(0)

def get_coords(x, y):
    '''
    Parameters
    ----------
    x: int
        x-coordinate of the player
    y: int
        y-coordinate of the player
    '''
    player.ondrag(None)
    player.setheading(player.towards(x, y))
    player.goto(x, y)
    player.ondrag(get_coords)

onscreenclick(get_coords)

#create functions for keyboard movement
def turnleft():
    player.left(15)
    
def turnright():
    player.right(15)

def go_up():
    player.forward(15)

def go_down():
    player.backward(15)

#function for turtle and object collision
def collide(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2[i].xcor(), 2) + math.pow(t1.ycor() - t2[j].ycor(), 2))
    if d < 20:
        return True
    else:
        return False

#user inputted variables in pop up windows
num = turtle.textinput("How many objects would you like?", "# of objects between 1-100")
speed = turtle.textinput("How fast would you like the objects to move?", "Objects can go at a speed from 0-10 with 0 being the fastest and 1-10 subsequently increasing in speed")
    
wn.tracer(int(speed))

#use keyboard
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(go_up, "Up")
turtle.onkey(go_down, "Down")

balls = []
        
for _ in range(int(num)):
    balls.append(turtle.Turtle())
      
colors = ["red", "blue", "green", "yellow", "purple", "orange", "white", "aquamarine", "cornflower blue", "maroon"]
    
shapes = ["circle", "triangle", "square"]
    
for ball in balls:
    ball.shape(random.choice(shapes)) #random shapes
    ball.color(random.choice(colors)) #random colors
    ball.penup()
    ball.speed(0)
    x = random.randint(-305, 305)
    y = random.randint(100, 400)
    ball.goto(x, y) #random x, y location starting point

    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5) #random rotation


gravity = 0.1 #-9.8 #meters/s^2

while True:
    wn.update()
    
    #creating boundary for player
    if player.xcor() > 330:
        player.right(180)
    if player.xcor() < -330:
        player.setx(-330) #fixes issue where the object would get stuck
        player.right(180)
    if player.ycor() > 290:
        player.right(180)
    if player.ycor() < -290:
        player.sety(-290) #fixes issue where the object would get stuck
        player.right(180)
    
    #movement of objects
    for ball in balls:
        ball.rt(ball.da) #gets it to rotate
        
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        
        ball.setx(ball.xcor() + ball.dx) 
        
        #checking for wall
        if ball.xcor() > 340:
            ball.dx *= -1
            ball.da *= -1

        if ball.xcor() < -350:
            ball.setx(-350) #fixes issue where the object would get stuck
            ball.dx *= -1
            ball.da *= -1 #rotation

        #checking for bounce
        if ball.ycor() < -300:
            ball.sety(-300) #fixes issue where the object would get stuck
            ball.dy *= -1
            ball.da *= -1 #rotation
            
    #checking for collisions between objects
    for i in range(0, len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i].distance(balls[j]) < 20:
                temp_dx = balls[i].dx
                temp_dy = balls[i].dy
                
                balls[i].dx = balls[j].dx
                balls[i].dy = balls[j].dy
                
                balls[j].dx = temp_dx
                balls[j].dy = temp_dy
                
    #checking for collisions between player and objects
    for i in range(0, len(balls)):
        for j in range(0, len(balls)):
            if collide(player, balls):
                temp_dx = balls[i].dx
                temp_dy = balls[i].dy

                balls[i].dx = balls[j].dx
                balls[i].dy = balls[j].dy

                balls[j].dx = temp_dx
                balls[j].dy = temp_dy
    
            
wn.mainloop()