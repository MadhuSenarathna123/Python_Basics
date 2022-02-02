temp = float(input("enter tempurature = "))
unit= input("enter c for celsius  or f for faranhight")
if unit== "c":
    print("f = ",(temp*9/5)+32)
else :
    print("c = ",(temp-32)*5/9)