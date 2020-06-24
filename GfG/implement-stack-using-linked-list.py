class MyStack:
    def __init__(self):
        self.l = []

    # The method push to push element into
    # the stack
    def push(self, data):
        self.l.append(data)

    def pop(self):
        try:
            return self.l.pop()
        except:
            return -1

    def isEmpty(self):
        if(len(self.l) == 0):
            return True
        else:
            return False

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()
