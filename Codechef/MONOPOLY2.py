t = int(input())
for i in range(t):
    p,q,r,s = map(int, input().split())
    max_p = max(p,q,r,s)
    sum_t = p + q+ r + s
    if (max_p > (sum_t - max_p)):
        print("YES")
    else:
        print("NO")