// { Driver Code Starts
#include<bits/stdc++.h>

using namespace std;

struct Node
{
    int data;
    Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
};


void print(Node *root)
{
    Node *curr = root;
    while(curr!=NULL)
    {
        cout<<curr->data<<" ";
        curr=curr->next;
    }
}


Node *compute(Node *head);

int main()
{
    int T;
	cin>>T;

	while(T--)
	{
		int K;
		cin>>K;
		struct Node *head = NULL;
        struct Node *curr = head;

		for(int i=0;i<K;i++){
		    int data;
		    cin>>data;
			if(head==NULL)
			    head=curr=new Node(data);
			else
			{
				curr->next = new Node(data);
				curr = curr->next;
			}
		}

        Node *result = compute(head);
        print(result);
        cout<<endl;
    }
}
// } Driver Code Ends


/*

The structure of linked list is the following

struct Node
{
    int data;
    Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
};
*/
Node *compute(Node *head)
{
    Node *curr = head, *temp;
    int flag = 1;
    while(flag){
    	flag = 0;
	    while(curr && curr->next){
	    	if(curr->next->data > curr->data){
	    		temp = curr->next;
	    		curr->data = temp->data;
	    		curr->next = temp->next;
	    		free(temp);
	    		flag = 1;
	    	}
	    	else{
	    		curr = curr->next;
	    	}
	    }
	    curr = head;
	}
    return head;
}