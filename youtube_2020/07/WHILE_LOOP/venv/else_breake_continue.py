# a=5
# b=10
# while a<b:
#     print(a)
#     a=a+1
#     continue#continue use inside the loop. beacuse the loop statement goint to while after meeting while
#     print("inside the loop")
#
# else:
#     print("in the else condition")

a=5
b=10
while a<b:
    print(a)
    a=a+1
    print("inside the loop")
    break  # breake whole loop

else:
    print("in the else condition")
