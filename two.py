m = int(input("Value of M: "))
count, maxp , maxptable , maxpchair= 1 , 0 , 0 , 0

for i in range (0,121):
    for j in range (0,121):
        if((4*i + j <= 200) and (2*i + j <= 120)):
            ptable = 90*i if(i<=m) else 90*m + 100*(i-m)
            pchair = 25*j if(j<=m) else 25*m + 30*(j-m)
            p = ptable + pchair
            if(p>maxp):
                maxp = p
                x1 = i
                x2 = j
                    
print("X1:",x1,"\nX2:",x2,"\nMaximum Profit: ",maxp)