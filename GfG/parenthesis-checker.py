t = int(input())
for i in range(t):
    expr = input()
    lst = list()
    flag = 0
    for j in expr:
        if j == "(" or j == "[" or j == "{":
            lst.append(j)
        elif j == ")" and (len(lst) == 0 or lst.pop() != "("):
            print("not balanced")
            flag = 1
            break
        elif j == "]" and (len(lst) == 0 or lst.pop() != "["):
            print("not balanced")
            flag = 1
            break
        elif j == "}" and (len(lst) == 0 or lst.pop() != "{"):
            print("not balanced")
            flag = 1
            break
    if flag == 0 and len(lst) == 0:
        print("balanced")
    else:
        print("not balanced")