#include <stdlib.h>
#include <stdio.h>
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
typedef struct node{
	int h;
	int k;
	struct node *next;
}node;

void merge(int **people, int l, int m, int r){
	int i = l;
	int j = m+1;
	int **temp = (int**)calloc((r-l+2), sizeof(int*));
	int k = 0;
	while(i <= m && j <= r){
		if(people[i][0] < people[j][0]){
			temp[k] = (int*)malloc(3 * sizeof(int));
			temp[k][0] = people[i][0];
			temp[k++][1] = people[i++][1];
		}
		else if(people[i][0] > people[j][0]){
			temp[k] = (int*)malloc(3 * sizeof(int));
			temp[k][0] = people[j][0];
			temp[k++][1] = people[j++][1];
		}
		else{
			if(people[i][1] > people[j][1]){
				temp[k] = (int*)malloc(3 * sizeof(int));
				temp[k][0] = people[i][0];
				temp[k++][1] = people[i++][1];
			}
			else{
				temp[k] = (int*)malloc(3 * sizeof(int));
				temp[k][0] = people[j][0];
				temp[k++][1] = people[j++][1];
			}
		}
	}
	while(i <= m){
		temp[k] = (int*)malloc(3 * sizeof(int));
		temp[k][0] = people[i][0];
		temp[k++][1] = people[i++][1];
	}
	while(j <= r){
		temp[k] = (int*)malloc(3 * sizeof(int));
		temp[k][0] = people[j][0];
		temp[k++][1] = people[j++][1];
	}
	for(i = l, k = 0; i <= r;++i, ++k){
		// printf("%d %d\n", i, k);
		people[i][0] = temp[k][0];
		people[i][1] = temp[k][1];
		free(temp[k]);
	}
	free(temp);
}

void mergesort(int **people, int l, int r){
	if(l < r){
		int m = (l+r)/2;
		mergesort(people, l, m);
		mergesort(people, m+1, r);
		merge(people, l, m, r);
	}
}

node* create(int *key){
	node *temp = (node*)malloc(sizeof(node));
	temp->h = key[0];
	temp->k = key[1];
	temp->next = NULL;
	return temp;
}

void insert(node **addr, int *key, int index){
	node *temp = create(key);
	// printf("%d\n", index);
	if(index == 0){
		temp->next = *addr;
		*addr = temp;
	}
	else{
		int i = 0;
		node *prev = NULL;
		node *head = *addr;
		node *curr = *addr;
		// printf("%d %d\n", curr->h, curr->k);
		while(i < index){
			prev = curr;
			curr = curr->next;
			++i;
		}
		prev->next = temp;
		temp->next = curr;
		*addr = head;
	}
}

int** reconstructQueue(int** people, int peopleSize, int* peopleColSize, int* returnSize, int** returnColumnSizes){
	*returnSize = peopleSize;
	*returnColumnSizes = (int*)malloc(peopleSize * sizeof(int));
	int **copy = (int**)malloc(peopleSize * sizeof(int*));
	for (int i = 0; i < peopleSize; ++i)
	{
		(*returnColumnSizes)[i] = 2;
		copy[i] = (int*)malloc(2 * sizeof(int));
		copy[i][0] = people[i][0];
		copy[i][1] = people[i][1];
	}
	mergesort(copy, 0, peopleSize-1);
	node *head = NULL;
	for(int i = peopleSize-1; i >= 0; --i){
		insert(&head, copy[i], copy[i][1]);
	}
	node *temp = head;
	node *temp1;
	for(int i = 0; i < peopleSize; ++i){
		copy[i][0] = temp->h;
		copy[i][1] = temp->k;
		temp1 = temp->next;
		free(temp);
		temp = temp1;
	}
	return copy;
}

int main(){
	int **people = (int**)malloc(6*sizeof(int**));
	int *arr = (int*)malloc(6*sizeof(int));
	int *arr1;
	int temp;
	for (int i = 0; i < 6; ++i)
	{
		people[i] = (int*)malloc(2*sizeof(int));
		arr[i] = 2;
		for (int j = 0; j < 2; ++j)
		{
			scanf("%d", &people[i][j]);
		}
	}
	int **copy = reconstructQueue(people, 6, arr, &temp, &arr1);
	for (int i = 0; i < 6; ++i)
	{
		for (int j = 0; j < 2; ++j)
		{
			printf("%d ", copy[i][j]);
		}
		printf("\n");
		free(copy[i]);
		free(people[i]);
	}
	free(copy);
	free(people);
	free(arr);
	free(arr1);
}