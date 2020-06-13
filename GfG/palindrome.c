#include <stdio.h>

int main(){
	int t;
	scanf("%d", &t);
	while(t--){
		int inp, temp, sum, inpCopy;
		scanf("%d",&inp);
		inpCopy = inp;
		sum = 0;
		while(inp){
			temp = inp%10;
			inp /= 10;
			sum = sum*10 + temp;
		}
		if(sum == inpCopy)
			printf("YES\n");
		else
			printf("NO\n");
	}
}