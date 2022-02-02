side=int(input("number of sides = "))
if side >=3 and side<=8:
    if side == 3:
        print("triangle")
    elif side == 4:
        print("rectangle")
    elif side == 5:
        print("pentagon")
    elif side == 6:
        print("hexagon")
    elif side == 7:
        print("heptagon")
    elif side == 8 :
        print("octagon")
else :
    print("enter correct value between 3 and 8")
