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

def drawspiral():
    step = 1
    currentnum = 0
    sr.goto(0, 0)
    while(sr.xcor() < 800 and sr.ycor() < 800 and sr.xcor() > -800 and sr.ycor() > -800):
        for _ in range(int(step)):
            currentnum += 1
            if(primecheck(currentnum)):
                sr.dot(6, "red")
                sr.forward(5)
            else:
                sr.dot(6)
                sr.forward(5)
            s.update()
        sr.left(90)
        step += 0.5
    print("Done")

drawspiral()

screen = sr.getscreen()
screen.getcanvas().postscript(file = "spiral.eps")

#main loop
while True:
    s.update()
