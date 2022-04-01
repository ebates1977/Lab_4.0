import turtle
t = turtle.Turtle()

def position(x,y): ## moves the pen to the top left corner 
  t.penup()
  t.goto(x, y)
  t.pendown()
  
def empty_square(n): ## creates an empty square, where side lengths are of size "n"
  
  x = 4
  for i in range (x):
    t.forward(n)
    t.left(90)

def filled_square(n): ##creates a filled square, where side lengths are of size "n"
  x = 4
  t.begin_fill()
  for i in range (x):
    t.forward(n)
    t.left(90)
  t.end_fill()

def move_left(n): ## moves the pen left to create the next square
  t.penup()
  t.forward(n)
  t.pendown()

def move_right(n): ## moves the pen right to create the next square
  t.penup()
  t.back(n)
  t.pendown()

def move_down(n): ## moves the pen down to create the next square
  t.penup()
  t.right(90)
  t.pendown()

def speed():
  t.speed(10)