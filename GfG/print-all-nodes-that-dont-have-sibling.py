#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the print the nodes which dont have a sibling node
# Note: You aren't required to print a new line after every test case
def printSibling(root):
    l = []
    res = []
    flag = 0
    if(root):
        l.append(root)
    while(len(l) > 0):
        temp = l.pop(0)
        if(temp.left and not(temp.right)):
            res.append(temp.left.data)
            flag = 1
        elif(not(temp.left) and temp.right):
            res.append(temp.right.data)
            flag = 1
        if(temp.left):
            l.append(temp.left)
        if(temp.right):
            l.append(temp.right)
    if(flag == 0):
        print(-1, end=" ")
    else:
        res.sort()
        for i in res:
            print(i, end=" ")

 
# Driver Code Starts
# Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
   def __init__(self, val):
       self.right = None
       self.data = val
       self.left = None

# Function to Build Tree  
def buildTree(s):
   #Corner Case
   if(len(s)==0 or s[0]=="N"):          
       return None
       
   # Creating list of strings from input
   # string after spliting by space
   ip=list(map(str,s.split()))
   
   # Create the root of the tree
#   print(ip)
   root=Node(int(ip[0]))                    
   size=0
   q=deque()
   
   # Push the root to the queue
   q.append(root)                            
   size=size+1
   
   # Starting from the second element
   i=1                                      
   while(size>0 and i<len(ip)):
       # Get and remove the front of the queue
       currNode=q[0]
       q.popleft()
       size=size-1
       
       # Get the current node's value from the string
       currVal=ip[i]
       
       # If the left child is not null
       if(currVal!="N"):
           
           # Create the left child for the current node
           currNode.left=Node(int(currVal))
           
           # Push it to the queue
           q.append(currNode.left)
           size=size+1
       # For the right child
       i=i+1
       if(i>=len(ip)):
           break
       currVal=ip[i]
       
       # If the right child is not null
       if(currVal!="N"):
           
           # Create the right child for the current node
           currNode.right=Node(int(currVal))
           
           # Push it to the queue
           q.append(currNode.right)
           size=size+1
       i=i+1
   return root

   
if __name__=="__main__":
   t=int(input())
   for _ in range(0,t):
       s=input()
       root=buildTree(s)
       printSibling(root)
       print()
# } Driver Code Ends