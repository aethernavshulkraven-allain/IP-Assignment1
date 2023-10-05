x , y , dist_trav , x0 , y0 = 0 , 0 , 0 , 5 , 5
dist_in = 1;
while(True):
    dist_in = int(input("Enter the distace traveled : "))
    if(dist_in<=0):
        break
    if(dist_in<=25):
        y += dist_in
        dist_trav += dist_in
    elif(dist_in >=26 and dist_in <= 50):
        y -= dist_in
        dist_trav += dist_in
    elif(dist_in >=51 and dist_in <= 75):
        x += dist_in
        dist_trav += dist_in
    else:
        x -= dist_in
        dist_trav += dist_in

stldist = (x**2 + y**2)**(1/2)
print("Final Coordinates: ","(",x,",",y,")","\nDistance traveled: ",abs(dist_trav),"\nStraight line distance: ",stldist)
