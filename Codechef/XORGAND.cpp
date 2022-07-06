#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, q, l, r, x;
	cin >> t;
	while (t--) {
		cin >> n;
		int *arr = (int*)malloc(sizeof(int) * n);
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
		}
		cin >> q;
		
		while (q--) {
			int count = 0;
			cin >> l >> r >> x;
			for (int i = l-1; i < r; i++) {
				if ((arr[i] | x) > (arr[i] & x)) {
					count++;
				}
			}
			cout << count << endl;
		}
	}
	return 0;
}