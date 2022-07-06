#include<stdio.h>

int main(int argc, char const *argv[])
{
	int t, n, temp;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		int arr[10] = {0};
		for (int i = 0; i < n; i++) {
			scanf("%d", &temp);
			arr[temp-1]++;
		}
		int max1, max2, z1;
		max1 = max2 = 0;
		for (int i = 0; i < 10; i++) {
			if (arr[i] >= max1) {
				max2 = max1;
				max1 = arr[i];
				z1 = i+1;
			}
		}
		if (max1 == max2) {
			printf("CONFUSED\n");
		} else {
			printf("%d\n", z1);
		}
	}
	return 0;
}