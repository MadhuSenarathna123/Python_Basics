x=input("enter the posision = ")
letter=x[0]
number=int(x[1])
odd=[1,3,5,7]
even=[2,4,6,8]
let1=["a","c","e","g"]
let2=["b","d","f","h"]
if (number in odd and letter in let1) or (number in even and letter in let2):
    print("black squre")
elif (number in odd and letter in let2) or (number in even and letter in let1):
    print("white squre")
else:
    print("please enter valide posision")
