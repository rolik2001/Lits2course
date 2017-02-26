from turtle import *
x = float(input("Введіть кількість ітерацій:"))
y = float(input("Введіть швидкість:"))

def draw(t, b):
    if b == 0:
      forward(t)
      return
    draw(t, b - 1)
    left(60)
    color('red')
    draw(t, b - 1)
    right(120)
    color('yellow')
    draw(t, b - 1)
    left(60)
    color('green')
    draw(t, b - 1)

for i in range(3):
     speed(y)
     pensize(3)
     draw(5,x)
     right(120)
done()

