#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, x, y;
	cin >> t;
	while (t--) {
		cin >> x >> y;
		cout << x*10 + y*90 << endl;
	}
	return 0;
}