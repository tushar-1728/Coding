#include <stdio.h>

int main(int argc, char const *argv[])
{
	int t, x, y, z;
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d %d", &x, &y, &z);
		int weight = z-y;
		printf("%d\n", weight/x);
	}
	return 0;
}