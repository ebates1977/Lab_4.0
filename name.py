import turtle
import shapes

t = turtle.Turtle()

def a():
  t.penup()
  t.goto(140, 0)
  t.pendown()
  t.left(60)
  t.forward(100)
  t.right(120)
  t.forward(100)
  t.back(50)
  t.left(245)
  t.forward(60)

def m(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.left(90)
  t.forward(100)
  t.left(225)
  t.forward(50)
  t.left(90)
  t.forward(50)
  t.left(225)
  t.forward(100)

def e():
  t.penup()
  t.goto(-100, 0)
  t.pendown()
  t.left(90)
  t.forward(100)
  t.right(90)
  t.forward(60)
  t.left(180)
  t.forward(60)
  t.left(90)
  t.forward(50)
  t.left(90)
  t.forward(30)
  t.left(180)
  t.forward(30)
  t.left(90)
  t.forward(50)
  t.left(90)
  t.forward(60)
  


e()
m(-20, 0)
t.left(90)
m(60,0)
t.left(90)
a()
turtle.getscreen()._root.mainloop()