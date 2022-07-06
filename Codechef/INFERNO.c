#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
	int t, n, x, temp;
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d", &n, &x);
		int count, max;
		count = max = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &temp);
			if (temp > max) {
				max = temp;
			}
			if (temp > x) {
				count += temp/x;
				if (temp%x) {
					count++;
				}
			} else {
				count++;
			}
		}
		printf("%d\n", (int)fmin(count, max));
	}
	return 0;
}