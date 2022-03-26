import turtle
t = turtle.Turtle()

def position(x,y):
  t.penup()
  t.goto(x, y)
  t.pendown()

position(-75, 75)
n = 8
for i in range (n):
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.left(90)

turtle.getscreen()._root.mainloop()