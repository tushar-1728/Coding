#User function Template for python3
def freturn(ele0):
    return ele0[0]

def overlappedInterval(parr,n):
    parr.sort(key=freturn)
    print("parr:", parr)
    i = 1
    while(i < len(parr)):
        if(parr[i][0] <= parr[i-1][1]):
            parr[i][0] = parr[i-1][0]
            parr[i][1] = max(parr[i-1][1], parr[i][1])
            parr.pop(i-1)
        else:
            i += 1
    return parr


# Driver Code Starts
# Initial Template for Python 3

if __name__=='__main__':
    t= int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        parr=[]

        i=0
        while i<2*n:
            parr.append([arr[i],arr[i+1]])
            i+=2

        ans=overlappedInterval(parr,n)

        for e in ans:
            print(*e,end=' ')
        print()


# Driver Code Ends