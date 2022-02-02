u=float(input("enter tempuerature = "))
b = input("b if c for celcious f for farenhight = ")
if b=="c":
    t=u*(9/5)+32
    print(t)
elif b =="f":
    tc=(u-32)*(5/9)
    print(tc)
else:
    print("invalide")