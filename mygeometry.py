import math

def calcAreaofCircle(radius):
    result = 0.0
    pi = math.pi
    result = 2 * pi * radius
    return result

def calcperimeterofCircle(radius):
    result = 0.0
    perimeter = 2 * math.pi * radius
    return perimeter

area = calcAreaofCircle(8)
perimeter = calcperimeterofCircle(8)

print(area)
print(perimeter)
    

