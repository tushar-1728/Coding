#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, temp, count;
	int mod = 1000000000 + 7;
	string c;
	cin >> t;
	while (t--) {
		cin >> n;
		cin >> c;
		count = 01;
		for (int i = 0; i < n; ++i) {
			temp = c[i] - 97;
			if (temp == 0 || temp == 4 || temp == 8 || temp == 14 || temp == 20) {
				count += 0;
			} else if (temp > 0 && temp < 4) {
				if (temp-0 == 4-temp)
					count *= 2;
				// else
				// 	count += 1;
			} else if (temp > 4 && temp < 8) {
				if (temp-4 == 8-temp)
					count *= 2;
				// else
				// 	count += 1;
			} else if (temp > 8 && temp < 14) {
				if (temp-8 == 14-temp)
					count *= 2;
				// else
				// 	count += 1;
			} else if (temp > 14 && temp < 20) {
				if (temp-14 == 20-temp)
					count *= 2;
				// else
				// 	count += 1;
			}

			if (count > mod)
				count = count%mod;
		}
		cout << count << endl;
	}
	return 0;
}