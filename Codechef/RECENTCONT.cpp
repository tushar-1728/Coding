#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, lc, sc;
	string c;
	cin >> t;
	while (t--) {
		lc = sc = 0;
		cin >> n;
		for(int i =0; i < n; ++i) {
			cin >> c;
			if (c[0] == 'S')
				sc++;
			else
				lc++;
		}
		cout << sc << " " << lc << endl;
	}
	return 0;
}