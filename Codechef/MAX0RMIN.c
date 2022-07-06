#include <stdio.h>

int main(int argc, char const *argv[])
{
	int t, n, x;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		int count1 = 0, count0 = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &x);
			if (x == 1) {
				count1++;
			} else {
				count0++;
			}
		}
		if (count1 >= count0) {
			printf("%d\n", 1);
		} else {
			printf("%d\n", 0);
		}
	}
	return 0;
}