#include <iostream>
using namespace std;

int compare(int a, int b, int c, int d) {
	if ((a == c && b == d) || (a == d && b == c)) {
		return 1;
	}
	return 0;
}

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	while (t--) {
		int x, y, x1, y1, x2, y2;
		cin >> x >> y >> x1 >> y1 >> x2 >> y2;
		if (compare(x, y, x1, y1)) {
			cout << 1 << endl;
		} else if (compare(x, y, x2, y2)) {
			cout << 2 << endl;
		} else {
			cout << 0 << endl;
		}
	}
	return 0;
}