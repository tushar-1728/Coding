#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, x, y;
	scanf("%d", &t);
	while(t--) {
		scanf("%d %d", &x, &y);
		if (y <= (x * 107)/100) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
	return 0;
}