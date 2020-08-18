def m_abs(num):
    if num > 0:
        return num
    else:
        return 0


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    max_height_left = 0
    max_height_right = 0
    amount = 0
    left_max = []
    right_max = []
    for i in range(n):
        if arr[i] > max_height_left:
            left_max.append(arr[i])
            max_height_left = arr[i]
        else:
            left_max.append(max_height_left)
        if arr[n-i-1] > max_height_right:
            right_max.insert(0, arr[n-i-1])
            max_height_right = arr[n-i-1]
        else:
            right_max.insert(0, max_height_right)
    for i in range(1, n-1):
        amount += m_abs(min(left_max[i], right_max[i]) - arr[i])
    print(amount)