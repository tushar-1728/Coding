#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, i, count, flag;
	int arr[100000];
	cin >> t;
	while (t--) {
		cin >> n;
		for(int i = 0; i < n; i++) {
			cin >> arr[i];
		}
		flag = count = i = 0;
		while (i < n) {
			while (i+1 < n && arr[i] == arr[i+1]) {
				i++;
				flag = 1;
			}
			if (flag) {
				flag = 0;
				count += 1;
				i += 1;
			} else {
				count += 1;
				i += 1;
			}
		}
		cout << count << endl;
	}
	return 0;
}