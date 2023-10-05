def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def sine(x):
    sin = 0
    for i in range(7):
        sin += (((-1)**i)/factorial(2*i+1))*(x**(2*i+1))
    return sin

def cosine(x):
    cos = 0
    for i in range(7):
        cos += (((-1)**i)/factorial(2*i))*(x**(2*i))
    return cos

hor_dist = int(input("Enter the value of horizontal distance: "))
x = int(input("Enter the angle: "))
radx = (1.57/90)*x

height = hor_dist*(sine(radx)/cosine(radx))
slant = hor_dist/cosine(radx)

print("Hieght of tower: ",round(height,0))
print("Distance to the tip of the pole: ",round(slant,0))