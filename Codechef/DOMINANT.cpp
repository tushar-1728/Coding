#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char const *argv[])
{
    int t, a, b, c, sum;
    double max;
    cin >> t;
    while (t--) {
        cin >> a >> b >> c;
        max = fmax(a, fmax(b, c));
        sum = a + b + c;
        if (max > (sum - max)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
