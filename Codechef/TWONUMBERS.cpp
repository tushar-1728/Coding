#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t,n;
	cin >> t;
	while(t--){
		cin >> n;
		if (n == 2)
		{
			printf("0\n");
		} else if(n%2 == 1)
		{
			printf("%d\n", n/2 * (n/2 + 1) - 1);
		} else if ((n/2)%2 == 0)
		{
			printf("%d\n", (n/2 - 1) * (n/2 + 1) - 1);
		} else
		{
			printf("%d\n", (n/2 - 2) * (n/2 + 2) - 1);
		}
	}
	return 0;
}