x = 0
avg = 0

while(True):
    mark = int(input("enter marks = "))
    if mark != 0:
        avg = (mark +avg)
        x = x+1

    else:
        print(avg/x)