import turtle
t = turtle.Turtle()

def position(x,y):
  t.penup()
  t.goto(x, y)
  t.pendown()



def steps_down(x):
  
  position(-75, 75)
  n = x
  for i in range (n):
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
  
  turtle.getscreen()._root.mainloop()
steps_down(10)