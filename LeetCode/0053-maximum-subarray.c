#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int maxSubArray(int* nums, int numsSize){
	int lmin = 0;
	int gmin = INT_MIN;
	for(int i = 0; i < numsSize; ++i){
		lmin = lmin + nums[i];
		lmin = lmin > nums[i] ? lmin:nums[i];
		gmin = lmin > gmin ? lmin:gmin;
	}
	return gmin;
}

int main(){
	int size;
	scanf("%d", &size);
	int *nums = (int*)malloc(size*sizeof(int));
	for(int i = 0; i < size; ++i){
		scanf("%d", &nums[i]);
	}
	printf("%d\n",maxSubArray(nums, size));
}