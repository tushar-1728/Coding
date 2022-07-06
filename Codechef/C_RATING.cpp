#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, x, y;
	cin >> t;
	while (t--) {
		cin >> x >> y;
		y -= x;
		cout << y/8 + (y%8 == 0) << endl;
	}
	return 0;
}