mark = int(input("Enter Marks: "))


if mark <= 100 and mark >= 1:
    if mark >= 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Enter Correct Marks")