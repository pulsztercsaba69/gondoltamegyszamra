#ez egy rajztábla
import turtle
t = turtle.Turtle()
y = turtle.Turtle()
t.penup
y.penup()
tsize = 10
screen = turtle.Screen()
t.speed("fastest")
t.color("black")
tcolour = (0,0,0)
t.pensize(10)
y.speed("fastest")
y.color("black")
t.goto(0,0)
y.goto(200,-200)
t.clear()
t.shape("triangle")
y.hideturtle()
y.pendown()
y.dot(5)

def colourset():
  colour = input("Input colour string (DON'T TYPE IT HERE!) \n")
  print(colour)
  global tcolour
  tcolour = (int(colour[0:3]), int(colour[3:6]), int(colour[6:9]))
  t.color(tcolour)
  y.color(tcolour)
  y.dot(t.pensize()/2)

def peninc():
  tsize = t.pensize() + 2
  t.pensize(tsize)
  y.clear()
  y.dot(tsize/2)
def pendec():
  tsize = t.pensize() - 2
  t.pensize(tsize) 
  y.clear()
  y.dot(tsize/2)

def black():
  global tcolour
  tcolour = (0,0,0)
  t.color(tcolour)
  y.color(tcolour)
  y.dot(t.pensize()/2)
def jade():
  global tcolour
  tcolour = (0,255,200)
  t.color(tcolour)
  y.color(tcolour)
  y.dot(t.pensize()/2)
def white():
  global tcolour
  tcolour = (255,255,255)
  t.color(tcolour)
  y.color(tcolour)
  y.dot(t.pensize()/2)

def tclick(x,y):
  t.penup()
  t.goto(x,y)
  #t.color(230,230,230)
  #y.pencolor(230,230,230)
  #y.clear()
  y.dot(10)
  t.pendown()
def tdrag(x,y):
  global tcolour
  t.pendown()
  t.goto(x,y)
  t.color(tcolour)
  y.clear()
  y.color(tcolour)
  y.dot(tsize)

screen.onkey(peninc, "Right")
screen.onkey(pendec, "Left")
screen.onkey(t.clear, "space")
screen.onkey(black, "1")
screen.onkey(jade, "2")
screen.onkey(white, "3")
screen.onkey(colourset, "x")
t.ondrag(tdrag)
screen.onclick(tclick)

print("""Hey you! You're obviously really bored, since you're running my slightly trashy, slightly unfinished drawing program. (It's probably a rival to MS Paint though.)

Here are the controls:
Click to move the pen, click and drag to draw. Yes, click twice. Deal with it.
The left and right arrows decrease and increase pen size, respectively.
Space clears the canvas.
Pressing X lets you change the pen colour by inputting a colour string.
Quick colour shortcuts: 1-Black, 2-Jade, 3-White (eraser).
I have no idea how to program a 'save' so just screenshot the result.

A NOTE ON COLOUR STRINGS: 
First, input them CORRECTLY. RRRGGGBBB, no spaces, no letters, no values over 255. I didn't bother babyproofing this, as common sense exists.
Second, DON'T TYPE THEM IN HERE. The enter key causes the program to refresh, clearing the input in the process. See that little arrow/box icon in the corner? Click it and type the colour string there instead, then hit the enter button. (Ignore the error message, the color would have changed on the 'result'.) I don't know why, but it works.""")

screen.listen()