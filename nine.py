a , b , c , d , e = 10, 1.05, 1, 1.06 , 2.718281828459045

def demand(p):
    d = e**(a - b*p)
    return d

def supply(p):
    s = e**(c + d*p)
    return s

p = 1
flag = True
diff = 10**9

while(flag):
    diff_prev = diff
    dem = demand(p)
    sup = supply(p)
    diff = abs(dem - sup)
    if(diff_prev>diff):
        price = p
        dem_final = dem
        sup_final = sup
    else:
        flag = not flag
    
    p *= 1.05

print("Equilibrium Price:",price)
print("Equilibrium demand:",dem_final)
print("Equilibrium supply:",sup_final)