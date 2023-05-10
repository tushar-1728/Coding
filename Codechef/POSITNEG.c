#include <stdio.h>
#include <stdlib.h>

int main(void) {
	long long t, n, temp, p, q;
    scanf("%lld", &t);
    while (t--) {
        scanf("%lld", &n);
        p = q = 0;
        for (long long i = 0; i < n; i++)
        {
            scanf("%lld", &temp);
            if (temp > 0) p += (i+1);
            else q += (i+1);
        }
        printf("%lld\n", llabs(p-q));
    }
	return 0;
}
