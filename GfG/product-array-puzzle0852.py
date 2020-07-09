#User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

def threeSumClosest (arr, target):
    arr.sort()
    flag = 0
    sums = arr[0] + arr[1] + arr[-1]
    result = abs(target - sums)
    for i in range(n-1):
        a_pointer = i + 1
        b_pointer = len(arr) - 1
        while a_pointer < b_pointer:
            curr_sum = arr[i] + arr[a_pointer] + arr[b_pointer]
            temp = abs(target - curr_sum)
            if temp == result:
                sums = max(curr_sum, sums)
            if temp < result:
                result = temp
                sums = curr_sum
            if curr_sum > target:
                b_pointer -= 1
            else :
                a_pointer += 1
    return sums

    # Your Code Here


#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n, target = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    print (threeSumClosest (arr, target))
    

# } Driver Code Ends