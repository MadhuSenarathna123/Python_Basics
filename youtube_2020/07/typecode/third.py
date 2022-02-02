class Counter (object):
    def __init__(self):
        self._number=0
    def increment (self):
        self._number+=1
    def __str__(self):
        return str(self._number)
def fib(n,counter):
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n - 1, counter) + fib(n - 2, counter)

counter =Counter()
next_fib=fib(5,counter)
print(next_fib)


