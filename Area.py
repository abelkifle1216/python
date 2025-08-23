#function defintion for area squa
from math import pi
def square(side):
    return side **2
#function defintion for area of rectangle
def rectangle(length,width):
    rect = length * width
    return rect
#function defntion for area of triangle
def tri(width,length,base):
    tri = 0.5 *(base * length) * width
    return tri
#function defintion for area of circle
def circle(radius):
    area_circle = pi * radius**2
    return area_circle
#function defintion for area of tripizoid
def tripizoid(b1,b2,h):
    area_tripizoid = 0.5 * ( b1 + b2) * h
    return area_tripizoid
#function defintion for area of ellipies 
def ellipies(a,b):
    area_ellipies = pi * a * b
    return area_ellipies
