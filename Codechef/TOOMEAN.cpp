#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n;
	cin >> t;
	while (t--) {
		float sum = 0, count = 0;
		cin >> n;
		float *arr = (float*)malloc(sizeof(float) * n);
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
		}
		sort(arr, arr + n);
		for (int i = 0; i < n-1; i += 2) {
			arr[i] = (arr[i] + arr[i+1])/2;
		}
		for (int i = 0; i < n; i += 2) {
			sum += arr[i];
			count++;
		}
		cout << sum/count << endl;
		free(arr);
	}
	return 0;
}