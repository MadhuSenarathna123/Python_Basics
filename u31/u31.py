a=float(input("enter the price = "))
b=a%5
if b >= 2.5:
    print("new price = ",a+(5-b))
else:
    print("new price = ",(a-b))

