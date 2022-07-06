#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	while (t--) {
		int n, x;
		cin >> n >> x;
		x = x*3;
		cout << n/x;
	}
	return 0;
}