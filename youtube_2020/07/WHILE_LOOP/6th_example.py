# x = True
# y = False
# z = True
# while x:
#     while y:
#         print("won't print")
#     while z:
#         print("should print")

x = True
y = False
z = True
a=5
while x:
    while y:
        print("won't print")
    while a<10:
        print("should print")
        a=a+1

