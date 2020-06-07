#include <stdlib.h>
#include <stdio.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decompressRLElist(int* nums, int numsSize, int* returnSize){
	int len = 0;
	int i, j, k = 0;
	int temp;
	for(i = 0; i < numsSize; i += 2){
		len += nums[i];
	}
	*returnSize = len;
	int *res = (int*)malloc(len * sizeof(int));
	for(i = 1, j = 0; i < numsSize; i+=2, j+=2){
		temp = nums[j];
		while(temp--){
			res[k++] = nums[i];
		}
	}
	return res;
}