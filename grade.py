mark = int(input("Enter Marks: "))

if mark <= 100 and mark >= 1:
    if mark >= 75:
        print("A")
    elif mark >= 65:
        print("B")
    elif mark >= 50:
        print("C")
    elif mark >= 35:
        print("S")
    else:
        print("Fail")
else:
    print("Enter Correct Marks")
