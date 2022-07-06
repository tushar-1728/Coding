#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, x, y, s1, s2;
	cin >> t;
	while (t--) {
		cin >> x >> y;
		s1 = 500 - x*2 + 1000 - (x+y)*4;
		s2 = 1000 - y*4 + 500 - (x+y)*2;
		cout << (s1>s2?s1:s2) << endl;
	}
	return 0;
}
