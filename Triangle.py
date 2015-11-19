#phythagorus
from math import *
def hypotenuse(a,b):
   c=sqrt(a**2+b**2)
   return c


# perimeter
def rightTrianglePerimeter(a, b,):
    perimeter=a+b+hypotenuse(a,b)
    return perimeter

#Distance in 2 Dimensions
def distance2D(x1, y1, x2, y2) :
    a=(x1-x2)
    b=(y1-y2)
    return  hypotenuse(a, b)

#Perimeter of Any Triangle
def trianglePerimeter(xA, yA, xB, yB, xC, yC):
    a=distance2D(xA, yA, xB, yB)
    b=distance2D(xA, yA, xC, yC)
    c=distance2D(xC, yC, xB, yB)
    perimeter=a+b+c  
    return perimeter

print trianglePerimeter(2, 0, 2, 0, 1, 5)
