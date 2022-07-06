#include <stdio.h>

int main(int argc, char const *argv[])
{
	int t, n, m, x;
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d %d", &n, &m, &x);
		if (m <= x) {
			printf("%d\n", 0);
		} else {
			int avg_tot = n * x;
			int tot = (n-1) * (x + 1);
			int students = n - 1;
			while (tot > avg_tot) {
				tot -= (x+1);
				students -= 1;
			}
			printf("%d\n", students);
		}
	}
	return 0;
}