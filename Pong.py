import turtle  #importing Turtle Module to build graphics

#Setting up game window
wn= turtle.Screen()
wn.title("Virtual Pong Game made with Python, by Adrija")
wn.bgcolor("black")
wn.setup(width=800, height= 600)
wn.tracer(0)

#Keeping Score
score_a=0
score_b=0

#Paddle A
paddle_A= turtle.Turtle()   #turtle=module name, Turtle= class name; creation of object
paddle_A.speed(0)           #sets speed of compiler (NOT game) to maximum possible speed
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.penup()      #makes sure that the created moving object does not draw anything onscreen
paddle_A.goto(-360,0)  #X and Y-axis
paddle_A.shapesize(stretch_len= 1, stretch_wid= 5)
#Paddle B
paddle_B= turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.penup()
paddle_B.goto(360,0)
paddle_B.shapesize(stretch_len=1, stretch_wid=5)
#Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#Pen
pen= turtle.Turtle()
pen.speed(0)            #Animation speed
pen.color("white")
pen.penup()
pen.hideturtle()        #Show only text, hide main object form screen
pen.goto(0,260)
pen.write("Player A: 0   Player B= 0", align="center", font=("Courier", 24, "bold"))


#Ball Movement
ball.dx= 0.08               #Ball moves by 2 pixels in (+ve) X-direction (Right)
ball.dy= 0.08                 #Ball moves by 2 pixels in (+ve) Y-direction (Up)
#Function
def paddle_a_up():
    y= paddle_A.ycor()     #Returns value of Y-Coordinate
    y+=20                  #add 20 pixels to Y-coordinate
    paddle_A.sety(y)       #Set value of y to the new y
def paddle_a_down():
    y= paddle_A.ycor()
    y-=20
    paddle_A.sety(y)

def paddle_b_up():
    y= paddle_B.ycor()     #Returns value of Y-Coordinate
    y+=20                  #add 20 pixels to Y-coordinate
    paddle_B.sety(y)       #Set value of y to the new y
def paddle_b_down():
    y= paddle_B.ycor()
    y-=20
    paddle_B.sety(y)

#Keyboard binding
wn.listen()                     #Instructs program to "listen" for keyboard input
wn.onkeypress(paddle_a_up,"w")    #If user presses "w", the paddle_a_up function is called

wn.listen()
wn.onkeypress(paddle_a_down, "q")

wn.listen()
wn.onkeypress(paddle_b_up, "e")

wn.listen()
wn.onkeypress(paddle_b_down, "r")

#Main Game Loop
while True:
    wn.update()

    #Move the Ball
    ball.setx(ball.xcor()+ ball.dx)    # ball.xcor()= current x-coordinate+ 2 units upwards (i.e., ball.dx)
    ball.sety(ball.ycor()+ ball.dy)    # ball.ycor()= current y-coordinate+ 2 units upwards (i.e., ball.dy)

    #Border checking
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy *= -1        #Reverses ball direction
        

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1        #Reverses ball direction

    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a+=1
        pen.clear() #Prevent overwriting
        pen.write(f"Player A: {score_a}   Player B= {score_b}", align="center", font=("Courier", 24, "bold"))

    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.setx(290)
        ball.dy *=-1
        score_b +=1
        pen.clear() #Prevent overwriting
        pen.write(f"Player A: {score_a}   Player B= {score_b}", align="center", font=("Courier", 24, "bold"))

    #Paddle and Ball collisions
    if (ball.xcor()> 340 and ball.xcor()< 350) and (ball.ycor()<paddle_B.ycor() +50 and ball.ycor()> paddle_B.ycor() -50):    
    #Width of paddle= 10, half-court length= 350
        ball.setx(340)
        ball.dx *= -1
    #(ball.ycor()<paddle_b.ycor() +50 and ball.ycor()> paddle_b.ycor() -50)= Upper, Lower coordinates

    if (ball.xcor()< -340 and ball.xcor()> -350) and (ball.ycor()<paddle_A.ycor() +50 and ball.ycor()> paddle_A.ycor() -50):    
        ball.setx(-340)
        ball.dx *= -1

        