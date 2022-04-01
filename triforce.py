import turtle

t = turtle.Turtle()

def triforce():
  t.penup()
  t.goto(-75, 75)
  t.pendown()
  n = 3
  for i in range (n):
    t.forward(100)
    t.left(120)
  
  t.forward(50)
  t.left(60)
  
  for i in range (n):
    t.forward(50)
    t.left(120)

  turtle.getscreen()._root.mainloop()
triforce()


  