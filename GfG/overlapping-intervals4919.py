#User function Template for python3

def merge(parr, l, m, r):
    i = l
    j = m+1
    k = 0
    temp = []
    while(i <= m and j <= r):
        if parr[i][0] < parr[j][0]:
            temp.append(parr[i])
            i += 1
        elif parr[j][0] < parr[i][0]:
            temp.append(parr[j])
            j += 1
        else:
            if(parr[i][1] < parr[j][1]):
                temp.append(parr[i])
                i += 1
            else:
                temp.append(parr[j])
                j += 1
    while i <= m:
        temp.append(parr[i])
        i += 1
    while j <= r:
        temp.append(parr[j])
        j += 1
    for i in range(l, r+1):
        parr[i] = temp[k]
        k += 1

def mergesort(parr, l, r):
    if(l < r):
        m = (l+r) // 2
        mergesort(parr, l, m)
        mergesort(parr, m+1, r)
        merge(parr, l, m, r)

def overlappedInterval(parr,n):
    mergesort(parr, 0, n-1)
    # print("parr:", parr)
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