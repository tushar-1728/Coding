#include <iostream>
using namespace std;

int max(int a, int b) {
    return a > b ? a : b;
}

int main() {
    int t, p1, p2, q1, q2, pm, qm;
    cin >> t;
    while (t--) {
        cin >> p1 >> p2 >> q1 >> q2;
        pm = max(p1, p2);
        qm = max(q1, q2);
        if (pm < qm) {
            cout << "P" << endl;
        } else if (qm < pm) {
            cout << "Q" << endl;
        } else {
            cout << "TIE" << endl;
        }
    }
	// your code goes here
	return 0;
}
