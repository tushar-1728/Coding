#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n;
	cin >> t;
	while (t--) {
		cin >> n;
		int a[n];
		for (int i = 0; i < n; ++i)
		{
			cin >> a[i];
		}
		int sum = a[0] + a[n-1];
		for (int i = n-1; i > 0; --i) {
			int temp = a[i] + a[i-1];
			if (temp > sum) {
				sum = temp;
			}
		}
		cout << sum << endl;
	}
	return 0;
}