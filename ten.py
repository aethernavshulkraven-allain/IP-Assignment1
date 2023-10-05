x0 = int(input("Enter the value of X0: "))

def valueofpolynomial(x):
    ans1 = x**3 - 10.5*x**2 + 34.5*x - 35
    return ans1 

def derivativeofpolynomial(x):
    der = 3*(x**2) - 21*(x**2) + 34.5*x
    return der

val = valueofpolynomial(x0)
count = 0

while (-0.2> valueofpolynomial(x0) or valueofpolynomial(x0) >0.2) :
    x0=x0-(valueofpolynomial(x0) / derivativeofpolynomial(x0))
    count += 1
    if count>100:
        print ("No roots are there within 100 iterations") 
        break
else:
    print (x0)