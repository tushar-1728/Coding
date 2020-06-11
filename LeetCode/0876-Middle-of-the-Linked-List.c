
// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};



struct ListNode* middleNode(struct ListNode* head){
	struct ListNode *temp;
	int count = 1;
	while(head->next){
		head = head->next;
		++count;
		if(count == 2){
			temp = head;
		}
		else if(count % 2 == 0){
			temp = temp->next;
		}
	}
	return temp;
}