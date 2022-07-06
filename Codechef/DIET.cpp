#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, k, sum, flag;
	int arr[100];
	cin >> t;
	while (t--) {
		cin >> n >> k;
		for (int i = 0; i < n; ++i) {
			cin >> arr[i];
		}
		flag = -1;
		sum = 0;
		for (int i = 0; i < n && flag == -1; ++i) {
			sum += arr[i];
			sum -= k;
			if (sum < 0) {
				flag = i;
			}
		}
		if (flag == -1) {
			cout << "YES" << endl;
		} else {
			cout << "NO " << flag + 1 << endl;
		}
		// cout << i << endl;
	}
	return 0;
}