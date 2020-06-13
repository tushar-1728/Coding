#include<stdio.h>
#include<stdlib.h>

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i){
	    int n, sum;
	    scanf("%d %d", &n, &sum);
	    int arr[n];
	    for(int j = 0; j<n; ++j){
	    	scanf("%d", &arr[j]);
	    }
	    int j = 0, k = 0, temp = 0;
	    while(k<n && temp < sum){
	    	temp += arr[k++];
	    	while(j<n && temp > sum)
	    		temp -= arr[j++];
	    	if(temp == sum){
	    		break;
	    	}
	    }
	    if(temp == sum)
    		printf("%d %d\n", j+1, k);
	    else	
	    	printf("-1\n");
	}
	return 0;
}