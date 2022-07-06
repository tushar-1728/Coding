#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t, len, max, temp;
	cin >> t;
	while (t--) {
		cin >> len;
		max = 0;
		int n[1005] = {0};
		for (int i = 0; i < len; ++i) {
			cin >> temp;
			n[temp]++;
		}
		for (int i = 0; i <= 1000; ++i) {
			max = n[i] > max ? n[i] : max;
		}
		cout << (len - max) << endl;
	}
	return 0;
}
