cost = int(input("Enter the cost of laptop: "))
allowance = float(input("Enter your monthly allowance: "))
sf = float(input("Enter the saving fraction: "))
r = float(input("Enter the rate of interest of the bank: "))

saving = allowance*sf
months = 0
amount = 0
def comp_amt(p,r,t):
    #P(1 + (r/12) )12t
    amt = p*(1+(r/100))**(12*t)
    return amt

while(amount < cost):
    amount = comp_amt(saving,r,1)
    saving = amount + allowance*sf
    months += 1

print("No. of months: ",months)
if (amount>cost):
    print("Saving: ",amount-cost)