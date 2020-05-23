import turtle
from math import sqrt

window = turtle.Screen()
window.title('House')
turtle.shape('arrow')
side = 100
angle = 90
# turtle actions
# Начертим квадрат
turtle.forward(side)
turtle.left(angle)
turtle.forward(side)
turtle.left(angle)
turtle.forward(side)
turtle.left(angle)
turtle.forward(side)
# Вернемся для того, чтобы начертить крышу
turtle.penup()
turtle.right(angle * 2)
turtle.forward(side)
# Чертим крышу
turtle.pendown()
turtle.right(angle / 2)
turtle.forward(side / sqrt(2))
turtle.right(angle)
turtle.forward(side / sqrt(2))
# Встанем на позицию, чтобы начертить дверь
turtle.penup()
turtle.right(angle / 2)
turtle.forward(side)
turtle.right(angle)
turtle.forward(side/3)
# Чертим дверь
turtle.pendown()
turtle.right(angle)
turtle.forward(side/3*2)
turtle.left(angle)
turtle.forward(side/3)
turtle.left(angle)
turtle.forward(side/3*2)
# end of actions
window.exitonclick()
