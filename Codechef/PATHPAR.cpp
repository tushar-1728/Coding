#include <iostream>
using namespace std;

int main() {
    int t, n, k;
    cin >> t;
    while (t--) {
        cin >> n >> k;
        if (n%2 == 0) {
            cout << "YES" << endl;
        } else {
            if (k == 1) {
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }
        }
    }
	// your code goes here
	return 0;
}
