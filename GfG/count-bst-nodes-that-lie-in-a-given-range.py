#User function Template for python3

##Structure of node
'''
# Node Class:
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
'''
def inorder(root, temp):
    if root is not None:
        inorder(root.left, temp)
        temp.append(root.data)
        inorder(root.right, temp)
        

##Complete this function
def getCountOfNode(root,l,h):
    temp = []
    count = 0
    inorder(root, temp)
    for i in temp:
        if(l <= i <= h):
            count += 1
    return count


#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class:
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data)
    else:
        root.right=newNode(root.right,data)
        
    return root
    

    
def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
            
        lr=[int(x) for x in input().strip().split()]

        print(getCountOfNode(root,lr[0],lr[1]))
        testcases-=1

if __name__=="__main__":
    main()
# } Driver Code Ends