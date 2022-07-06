#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        if (n > 30) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
