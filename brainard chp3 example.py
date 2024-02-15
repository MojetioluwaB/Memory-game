1#try if conditionsl statement
import random
import turtle
import time




for x in range(5):
    a = random.randint(1,99)
    turtle.write(str(a), font=("Verdana",50, "normal"))
    turtle.up()
    turtle.goto(x* offset,0)
    time.sleep(3)
    turtle.clear()

#please enter the answers
    for x in range(level):
    answer = int(input("The numbers were: "))
