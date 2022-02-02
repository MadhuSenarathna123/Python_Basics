def ourmin(mylist):
    minpos=0
    current=1
    while current <len(mylist):
        if (mylist[current]<mylist[minpos]):
            minpos=current
        current+=1
    return minpos

val_list = [14,56,67,2,78,13]
pos=ourmin(val_list)
print("minimum value is : ",val_list[pos])
