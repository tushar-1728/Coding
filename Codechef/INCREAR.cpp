#include <iostream>
using namespace std;

int main() {
    int t, x, y;
    cin >> t;
    while (t--) {
        cin >> x >> y;
        if (x == y) {
            cout << 0 << endl;
        } else if (y > x) {
            cout << y-x << endl;
        } else {
            if (y%2 == x%2) {
                cout << (x-y)/2 << endl;
            } else {
                cout << (x-y)/2 + 2 << endl;
            }
        }
    }
	// your code goes here
	return 0;
}
