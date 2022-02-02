name = (input("Enter your name"))
first_letter = name[0]
length=len(name)
last_letter=name[length-1]
vowel=["a","e","i","o","u"]

if first_letter in vowel:
    print(first_letter)
elif last_letter in vowel:
    print(last_letter)
else :
    print("no vowel")
