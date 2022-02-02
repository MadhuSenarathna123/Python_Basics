''' Module fib.py '''
def even_fib(n):
    total = 0
    f1, f2 = 1, 2
    while f1 < n:
        if f1 % 2 == 0:
            total = total + f1
        f1, f2 = f2, f1 + f2
    return total

uLimit=int(input("enter the upper unlimited"))
print(even_fib(int(uLimit)))

