#include <iostream>
#include <map>
#include <utility>
using namespace std;

int main(int argc, char const *argv[])
{
    int t, n, count;
    cin >> t;
    while (t--) {
        cin >> n;
        count = 0;
        int arr1[n], arr2[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr1[i];
        }
        for (int i = 0; i < n; i++)
        {
            cin >> arr2[i];
        }
        map<pair<int, int>, int> test; 
        for (int i = 0; i < n; ++i) {
            count += test[make_pair(arr1[i], arr2[i])];
            test[make_pair(arr2[i], arr1[i])]++;
        }
        cout << count << endl;
    }
    return 0;
}
