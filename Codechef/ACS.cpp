#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t, p, opt;
	cin >> t;
	while (t--) {
		cin >> p;
		opt = p/100 + p%100;
		if (opt > 10) {
			printf("%d\n", -1);
		} else {
			printf("%d\n", opt);
		}

	}
	return 0;
}
