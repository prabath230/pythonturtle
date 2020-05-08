import turtle

new_obj = turtle.Turtle()
new_obj.screen.bgcolor("black")
new_obj.color("red")
new_obj.shape("triangle")
new_obj.shapesize(1)

new_obj.forward(100)
new_obj.setheading(90)
new_obj.hideturtle()
new_obj.forward(100)

turtle.done()