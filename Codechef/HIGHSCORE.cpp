#include <iostream>
using namespace std;

int max(int a, int b) {
	return a > b ? a : b;
}

int main(int argc, char const *argv[])
{
	int t, n, a, b, c, d;
	cin >> t;
	while(t--) {
		cin >> n;
		cin >> a >> b >> c >> d;
		cout << max(a, max(b, max(c, d))) << endl;
	}
	return 0;
}