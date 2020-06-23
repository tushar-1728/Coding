#include <stdio.h>

int sumUnderModulo(long long a,long long b)
{
    int M=1000000007;
    a = a%M;
    b = b%M;
    int res = (a+b)%M;
    return res;
    //your code here
}

int main() {
	int T;
	scanf("%d", &T);
	while(T--)
	{
	    long long a;
	    long long b;
	    scanf("%lld %lld", &a, &b);
	    printf("%d\n", sumUnderModulo(a,b));
	}
	return 0;
}