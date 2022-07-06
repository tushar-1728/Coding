#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char const *argv[])
{
    int t, a, b, m;
    int dist1, dist2, max, min;
    cin >> t;
    while (t--) {
        cin >> a >> b >> m;
        max = a > b ? a : b;
        min = a < b ? a : b;
        dist1 = max - min;
        dist2 = (m - max) + min;
        // cout << max << min << dist1 << dist2 << endl;
        if (dist1 < dist2) {
            cout << dist1 << endl;
        } else {
            cout << dist2 << endl;
        }
    }
    return 0;
}
