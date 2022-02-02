marks=1
total=0
student_count=0
while marks !=0:
    marks=int(input("enter your marks = "))
    if marks !=0 and marks<101:
        total=total+marks
        student_count+=1
        continue
    else:
        break

average=total/student_count
print("average of marks = ",average)