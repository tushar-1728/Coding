#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int t, x, n;
	cin >> t;
	while (t--) {
		cin >> n >> x;
		if (n%2 == x%2)
			printf("YES\n");
		else if (n%2 == 1 && x%2 == 0)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}