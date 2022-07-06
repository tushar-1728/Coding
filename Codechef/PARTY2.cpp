#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int t, n, x, k;
    cin >> t;
    while (t--) {
        cin >> n >> x >> k;
        if ((n * x) <= k) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
