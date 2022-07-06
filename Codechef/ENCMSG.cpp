#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n;
	char temp;
	string inp;
	cin >> t;
	while (t--) {
		cin >> n;
		cin >> inp;
		for (int i = 0; i < n-1; i+=2) {
			temp = inp[i];
			inp[i] = inp[i+1];
			inp[i+1] = temp;
		}
		for (int i = 0; i < n; ++i) {
			inp[i] = 97 + abs(inp[i]-97-25);
		}
		cout << inp << endl;
	}
	return 0;
}