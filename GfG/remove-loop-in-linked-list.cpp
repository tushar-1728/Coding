// { Driver Code Starts
// driver code

#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node* next;
    
    Node(int val)
    {
        data = val;
        next = NULL;
    }
};

void loopHere(Node* head, Node* tail, int position)
{
    if(position==0) return;
    
    Node* walk = head;
    for(int i=1; i<position; i++)
        walk = walk->next;
    tail->next = walk;
}

bool isLoop(Node* head)
{
    if(!head) return false;
    
    Node* fast = head->next;
    Node* slow = head;
    
    while( fast != slow)
    {
        if( !fast || !fast->next ) return false;
        fast=fast->next->next;
        slow=slow->next;
    }
    
    return true;
}

int length(Node* head)
{
    int ret = 0;
    while(head)
    {
        ret++;
        head = head->next;
    }
    return ret;
}

void removeLoop(Node* head);

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n, num;
        cin>>n;
        
        Node *head, *tail;
        cin>> num;
        head = tail = new Node(num);
        
        for(int i=0 ; i<n-1 ; i++)
        {
            cin>> num;
            tail->next = new Node(num);
            tail = tail->next;
        }
        
        int pos;
        cin>> pos;
        loopHere(head,tail,pos);
        
        removeLoop(head);
        
        if( isLoop(head) || length(head)!=n )
            cout<<"0\n";
        else
            cout<<"1\n";
    }
	return 0;
}
// } Driver Code Ends


/*
structure of linked list node:

struct Node
{
    int data;
    Node* next;
    
    Node(int val)
    {
        data = val;
        next = NULL;
    }
};

*/

void removeLoop(Node* head)
{
    Node *temp1 = head;
    Node *temp2 = head;
    Node *loop = NULL;
    int count = 0;
    while(temp2->next && temp1->next && temp1->next->next){
    	++count;
        temp2 = temp2->next;
        temp1 = temp1->next->next;
        if(temp1 == temp2){
        	loop = temp1;
            break;
        }
    }
    if(loop){
	    temp1 = temp2 = head;
	    for(int i = 1; i < count; ++i){
	    	temp2 = temp2->next;
	    }
	    if(loop == head){
	    	// printf("%d\n", temp2->data);
	    	// printf("%d\n", temp2->next->data);
	    	temp2->next = NULL;
	    	return;
	    }
	    else{
	    	// printf("ban\n");
	    	temp2 = temp2->next;
	    	while(temp1 != temp2){
	    		temp1 = temp1->next;
	    		temp2 = temp2->next;
	    	}
	    	while(temp1->next != temp2){
	    		temp1 = temp1->next;
	    	}
	    	temp1->next = NULL;
	    	return;
	    }
	}
    // code here
    // just remove the loop without losing any nodes
}
// 1
// 5
// 7 58 36 34 16
// 1