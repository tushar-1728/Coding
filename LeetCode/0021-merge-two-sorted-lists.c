#include <stdio.h>
#include <stdlib.h>

struct ListNode {
   int val;
   struct ListNode *next;
};

struct ListNode* create_node(){
    struct ListNode *node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = 0;
    node->next  = NULL;
    return node;
}

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    if(l1 || l2){
        struct ListNode *head, *curr, *prev;
        prev = NULL;
        curr = head = create_node();
        while(l1 && l2){
            if(l1->val < l2->val){
                curr->val = l1->val;
                l1 = l1->next;
            }
            else{
                curr->val = l2->val;
                l2 = l2->next;
            }
            curr->next = create_node();
            prev = curr;
            curr = curr->next;
        }
        while(l1){
            curr->val = l1->val;
            l1 = l1->next;
            curr->next = create_node();
            prev = curr;
            curr = curr->next;
        }
        while(l2){
            curr->val = l2->val;
            l2 = l2->next;
            curr->next = create_node();
            prev = curr;
            curr = curr->next;
        }
        prev->next = NULL;
        free(curr);
        return head;
    }
    return NULL;
}