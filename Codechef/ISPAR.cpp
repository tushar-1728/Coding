#include <iostream>
using namespace std;

int main() {
    long long int t, n, k, res;
    cin >> t;
    while (t--) {
        cin >> n >> k;
        if (k == 1) {
            res = n%2;
        } else if (k == 2){
            res = 1;
        } else {
            res = 2;
        }
        if (res == 0) {
            cout << "EVEN" << endl;
        } else {
            cout << "ODD" << endl;
        }
    }
	// your code goes here
	return 0;
}
