#User function Template for python3
    
def numberOf2sinRange(n):
    temp = ""
    count = 0
    for i in range(1, n+1):
        temp += str(i)
    for i in temp:
        if i == "2":
            count += 1
    return count


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print(numberOf2sinRange(n))
# } Driver Code Ends