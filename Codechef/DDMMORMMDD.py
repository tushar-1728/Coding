t = int(input())
for i in range(t):
    d, m, y = map(int, input().split('/'))
    if (d <= 12 and m <= 12):
        print("BOTH")
    elif (d > 12):
        print("DD/MM/YYYY")
    else:
        print("MM/DD/YYYY")