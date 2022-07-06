#include <stdio.h>

int main(int argc, char const *argv[])
{
	int i, x, h;
	scanf("%d", &i);
	while(i--){
		scanf("%d %d", &x, &h);
		if (x >= h) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
	return 0;
}