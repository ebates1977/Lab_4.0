import turtle
t = turtle.Turtle()

def position(x,y):
  t.penup()
  t.goto(x, y)
  t.pendown()
  
def steps(x,y,z):
  position(-75, 75)
  for i in range (x):
    t.forward(y)
    t.right(90)
    t.forward(z)
    t.left(90)
    

  turtle.getscreen()._root.mainloop()
steps(5, 100, 50)