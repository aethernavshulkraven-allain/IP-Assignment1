pop = [50, 1450, 1400, 1700, 1500, 600, 1200]
r = 2.5

def list_sum(lst):
    result = 0
    for i in lst:
        result += i
    return result

curr_pop , prev_pop = list_sum(pop) , 0

print("Current population: ",curr_pop)

y = 0
while(curr_pop > prev_pop):
    r = 2.5-(0.1*y)
    for i in range(len(pop)):
        temp = pop[i]
        pop[i] += temp*(r/100)
        r-=0.4
    prev_pop = curr_pop
    curr_pop = list_sum(pop)
    y+=1

print("Years after which the maximum population will be reached: ",y-1)
print("Maximum population reached: ",round(prev_pop,0))