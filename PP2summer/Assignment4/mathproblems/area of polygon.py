from math import *
n=int(input("Input number of sides: "))
s=int(input("Input the length of a side: "))
print("The area of the polygon is: "+str(int((n*s*s/(4*tan(pi/n))))))