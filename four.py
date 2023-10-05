import math

def vel(t):
    v = 2000*math.log(140000/(140000-2100*t)) - 9.8*t
    return v

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
i = a
delta = 0.25
dist = 0

while(i<b):
    dist += ((vel(i)+vel(i+delta))/2)*delta
    i += delta

print(dist)