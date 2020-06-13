#include <iostream>
using namespace std;

int bin_search(int A[], int left, int right, int k){
	int low = left;
	int high = right;
	int mid;
	while(low <= high){
		mid = (high+low)/2;
		if(k == A[mid])
			return mid;
		else if(k > A[mid])
			low = mid+1;
		else
			high = mid-1;

	}
	return -1;
}

int main(){
	int t;
	cin >> t;
	while(t--){
		int n, key;
		cin >> n;
		int arr[n];
		for(int i = 0; i < n; ++i){
			cin >> arr[i];
		}
		cin >> key;
		int res = bin_search(arr, 0, n-1, key);
		cout << res << endl;
	}
}