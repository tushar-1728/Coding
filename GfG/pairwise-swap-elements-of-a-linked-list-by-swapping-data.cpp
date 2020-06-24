// { Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

struct Node {
    int data;
    Node *next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};

Node *pairWiseSwap(Node *head);

void insert(Node **head) {
    int n, i, value;
    Node *temp;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &value);

        if (i == 0) {
            *head = new Node(value);
            temp = *head;
        } else {
            temp->next = new Node(value);
            temp = temp->next;
        }
    }
}

void printList(struct Node *temp) {
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

/* Drier program to test above function*/
int main(void) {
    /* Start with the empty list */
    int t;

    /* Created Linked list is 1->2->3->4->5->6->7->8->9 */
    scanf("%d", &t);

    Node *head = NULL;

    while (t--) {
        head = NULL;
        insert(&head);
        head = pairWiseSwap(head);
        printList(head);
    }
    return (0);
}
// } Driver Code Ends


/*
  Pairwise swap a linked list
  The input list will have at least one element
  node is defined as

struct node
{
    int data;
    struct node* next;

    node(int x){
        data = x;
        next = NULL;
    }

}*head;
*/

Node* pairWiseSwap(struct Node* head) {
	Node *curr = head, *temp;
	if(curr && curr->next){
		temp = curr->next;
		curr->next = temp->next;
		temp->next = curr;
		head = temp;
	}
	// printf("%d\n", curr->data);
	while(curr->next && curr->next->next){
		temp = curr->next->next;
		curr->next->next = temp->next;
		temp->next = curr->next;
		curr->next = temp;
		curr = curr->next->next;
		// printf("%d\n", curr->data);
	}
	return head;
    // The task is to complete this method
}