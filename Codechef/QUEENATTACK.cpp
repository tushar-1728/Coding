#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
	int t, n, x, y;
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d %d", &n, &x, &y);
		int sum;
		double x1, xn, y1, yn;
		sum = 2*n - 2;
		x1 = (double)(x-1);
		xn = (double)(n-x);
		y1 = (double)(y-1);
		yn = (double)(n-y);
		sum += (int)((fmin(x1, y1) + fmin(xn, yn)) + fmin(x1, yn) + fmin(y1, xn));
		printf("%d\n", sum);
	}
	return 0;
}