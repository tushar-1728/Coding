def countWays(m):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    mod = 1000000007
    lst = [0] * (m+2)
    lst[1] = 1
    for i in range(2, m+1, 2):
        lst[i] = lst[i-1] + 1
        lst[i+1] = lst[i]
    print(lst)
    return lst[m]

 
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        print(countWays(m))