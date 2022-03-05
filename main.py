import turtle

#setting up the screen
s = turtle.Screen()
s.setup(800, 800)
s.tracer(0)
s.bgcolor("light blue")

#keeping window open
rootwindow = s.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

#spiral thingymagic
sr = turtle.Turtle()
sr.hideturtle()
sr.color("Yellow")
sr.pensize(2)

#checking if a number is prime in the most basic way possible
def primecheck(number):
    if(number == 2):
        return True
    if(number % 2 == 0):
        return False
    i = 3
    while(i * i <= number):
        if(number % i == 0):
            return False
        i += 2
    return True

#drawing the spiral
def drawspiral():
    step = 1 #step is to know when to turn the turtle
    currentnum = 0 #the individual dots
    sr.goto(0, 0)

    #drawing until the turtle goes out of the screen
    while(sr.xcor() < 800 and sr.ycor() < 800 and sr.xcor() > -800 and sr.ycor() > -800):
        #drawing the side of the spiral
        for _ in range(int(step)):
            currentnum += 1 #updating the number
            if(primecheck(currentnum)):
                sr.dot(6, "red") #highlighting the prime numbers with red instead of yellow
                sr.forward(5) #move that shit forwards
            else:
                sr.dot(6)
                sr.forward(5) #move that shit forwards
            s.update() #you don't actually need this; getting rid of it would improve performance probably, but it would be boring
        sr.left(90)
        step += 0.5 #little trick to update it every 2; add 0.5 and round down
    print("Done")

drawspiral()

s.exitonclick() #when the program is done, just click anywhere to close it
