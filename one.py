n = int(input("Enter the number: "))
lones = ["zero","one","two","three","four","five","six","seven","eight","nine"]
ltens = [0,"ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
l10_20 = [0,"eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

#0 - 99

if n in [0,1,2,3,4,5,6,7,8,9]:
    print(lones[n])
elif n in [11,12,13,14,15,16,17,18,19]:
    print(l10_20[n%10])
elif n%10 == 0:
    print(ltens[n//10])
elif n%10 != 0:
    print(ltens[n//10],lones[n%10])