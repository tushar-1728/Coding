import math
def allFactors(A):
    l = []
    a = int(math.sqrt(A))
    for i in range(1,a):
        if(A%i == 0):
            if(i == 196):
                print(i)
                print(A//i)
            l.append(i)
            l.append(A//i)
    if(A%a == 0):
        if(a*a == A):
            l.append(a)
        else:
            l.append(a)
            l.append(A//a)
    l.sort()
    return l

print(allFactors(38808))