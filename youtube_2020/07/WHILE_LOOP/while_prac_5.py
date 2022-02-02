total=0
mark=0
t=0
while (True):
    mark = int(input("enter your ICT marks = "))
    if mark != 0 :
     total=total+mark
     t=t+1
    else:
        print("Total is = ",total/t)
        break