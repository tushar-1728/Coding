#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int arr[4], count = 0;
	for (int i = 0; i < 4; ++i) {
		cin >> arr[i];
		count += (arr[i] >= 10);
	}
	cout << count << endl;
	return 0;
}