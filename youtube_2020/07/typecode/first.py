import time

problemSize = 10000000
print("problem size", "sSecond")
for count in range (5):
    start=time.time()
    work= 1
    for x in range (problemSize):
        work+=1
        work-=1
    elapsed = time.time()-start

    print(problemSize,elapsed)
    problemSize*=2


