#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	while (t--) {
		int n, temp, arr[100001] = {0};
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> temp;
			arr[temp]++;
		}
		temp = 0;
		for (int i = 0; i <= 100000; i++) {
			if (arr[i] % 2 == 1) {
				cout << i;
			}
		}
		cout << endl;
	}
	return 0;
}