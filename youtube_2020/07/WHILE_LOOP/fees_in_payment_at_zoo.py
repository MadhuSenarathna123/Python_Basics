age=1
amount=0

while age !=0:
    age=int(input("enter age = "))
    if age <= 2:
        amount=amount+0
    elif age >3 and age < 12:
        amount=amount+50
    elif age >=65:
        amount=amount+100
    elif age>=12 and age <65:
        amount=amount+150
    else :
        print("please enter correct age")
        continue
else:
    print("total amount = ",amount)


