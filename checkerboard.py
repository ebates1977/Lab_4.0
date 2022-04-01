import turtle
import shapes

def checkerboard():
  shapes.speed()
  shapes.position(-100, 75)
  n = 50
  for i in range (2):
    shapes.empty_square(n)
    shapes.move_left(n)
    shapes.filled_square(n)
    shapes.move_left(n)

  shapes.move_down(n)
  shapes.move_right(n)
  shapes.move_left(n)
  shapes.move_down(n)
  
  for i in range (2): 
    shapes.empty_square(n)
    shapes.move_left(n)
    shapes.filled_square(n)
    shapes.move_left(n)


  shapes.position(-50, 25)
  
  for i in range (2):
    shapes.empty_square(n)
    shapes.move_right(n)
    shapes.filled_square(n)
    shapes.move_right(n)
    
  shapes.position(-50, -25)
  

  for i in range (2):
    shapes.filled_square(n)
    shapes.move_right(n)
    shapes.empty_square(n)
    shapes.move_right(n)

    
checkerboard()
turtle.getscreen()._root.mainloop()