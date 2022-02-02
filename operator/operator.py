# num1=int(input("enter the first value = "))
# operator=input("enter the operator = ")
# num2=int(input("enter the second value = "))
#
#
#
# if operator== "+":
#     print("equation : ",num1+num2)
# elif operator == "-":
#     print("substraction : ",num1-num2)
# elif operator== "*":
#     print("multiplication : ",num1*num2)
# elif operator == "/":
#     print("deviding : ",num1/num2)
# else :
#     print("enter correct operstor : ")

#-------------------------
num1=int(input("enter the first value = "))
operator=input("enter the operator = ")
num2=int(input("enter the second value = "))
print(eval(str(num1)+operator+str(num2)))