import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0 

 #make screen
screen = turtle.Screen()
screen.title("Snake game by Taylor Foster")
screen.bgcolor("purple")
screen.setup(width=600, height=600)
screen.tracer(0) #turns off updates
#segment or body

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("BentonSans", 24, "bold"))

#make snake head
def go_up():
    if head.direction !="down":
        head.direction = "up"
def go_down():
    if head.direction !="up":
        head.direction = "down"
def go_left():
    if head.direction !="right":
        head.direction = "left"
def go_right():
    if head.direction !="left":
        head.direction = "right"
    

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0) #head in middle of screen
head.direction = "stop"

#make food
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("yellow")
food.penup()
food.goto(0,100) #head in middle of screen




#make it move
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#keyboard findings
screen.listen()
screen.onkeypress(go_up,"w")
screen.onkeypress(go_down,"s")
screen.onkeypress(go_left,"a")
screen.onkeypress(go_right,"d")
        
#main game loop -repeats over and over, move the head, slow down the speed
while True:
    screen.update()

    #check for border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        #clear segments list
        segments.clear()

        #reset the score
        score = 0

        #reset the delay
        delay = 0.1

    

        pen.clear ()
        pen.write("Score:{} High Score:{}".format(score, high_score), align=("center"), font=("BentonSans", 24, "bold"))
    
    
    #check if snake eats the food
    if head.distance(food) < 20:

        #if they hit the food, food moves to random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay time to make game faster
        delay -=0.001

        #increase the score
        score += 10

        # if the score is greater than high score set new score
        if score > high_score:
            high_score = score

        pen.clear ()
        pen.write("Score:{} High Score:{}".format(score, high_score), align=("center"), font=("BentonSans", 24, "bold"))
        
    #move end segement is reverse first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

        #move 1st segment after the head to where the head is
    if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

    
    move()

    #check for head colloision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            #clear segments list
            segments.clear()

            #reset the delay
            delay = 0.1
    
            #reset the score
            score = 0

            pen.clear ()
            pen.write("Score:{} High Score:{}".format(score, high_score), align=("center"), font=("BentonSans", 24, "bold"))
    

        
        
    
    time.sleep(delay)
    
screen.mainloop()
