age =1
total = 0
while age>0:
    age = int(input("enter coustomer's age = "))
    if age != 0:

         if age <=2:
             total = total+0
         elif age <= 3 or age <12:
             total=total+50
         elif age >=65:
            total=total+100
         else:
            total=total+150
            continue
    else:
        break
print('payment is =  ',total)