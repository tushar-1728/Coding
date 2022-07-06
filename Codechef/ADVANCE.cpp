#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, x, y;
	cin >> t;
	while (t--) {
		cin >> x >> y;
		if (y >= x && y <= x+200) {
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
		}
	}
	return 0;
}