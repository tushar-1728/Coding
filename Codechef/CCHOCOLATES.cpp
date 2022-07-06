#include <iostream>
using namespace std;

int main() {
    int t, x, y, z, sum;
    cin >> t;
    while (t--) {
        cin >> x >> y >> z;
        sum = x * 5 + y * 10;
        cout << sum / z << endl;
    }
	// your code goes here
	return 0;
}