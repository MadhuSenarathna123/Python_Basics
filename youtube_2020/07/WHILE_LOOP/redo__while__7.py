# 2 adu -- free
# 3 - 12 -- 50
# 65 ta vedi 100
# anit hamoma 150


total = 0
age =1
while age != 0 :
    age = int(input("enter age = "))

    if age <= 2:
        total = total+0
    elif age > 3 and age <12:
        total = total+50
    elif age >=12 and age < 65:
        total = total+100
    elif age >= 65 :
        total = total+150

print(total)

