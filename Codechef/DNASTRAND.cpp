#include <iostream>
#include <string>
using namespace std;

int main() {
	// your code goes here
	int t, len;
	string n;
	cin >> t;
	while (t--) {
		cin >> len;
		cin >> n;
		for (int i = 0; i < n.length(); i++) {
			switch(n[i]) {
				case 'A':
					n[i] = 'T';
					break;
				case 'T':
					n[i] = 'A';
					break;
				case 'C':
					n[i] = 'G';
					break;
				case 'G':
					n[i] = 'C';
					break;
			}
		}
		cout << n << endl;
	}
	return 0;
}
