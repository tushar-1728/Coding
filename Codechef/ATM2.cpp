#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	while (t--) {
		int n, k, temp;
		cin >> n >> k;
		for (int i = 0; i < n; i++) {
			cin >> temp;
			if (temp <= k) {
				k -= temp;
				cout << "1";
			} else {
				cout << "0";
			}
		}
		cout << endl;
	}
	return 0;
}