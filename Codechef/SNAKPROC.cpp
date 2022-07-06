#include <iostream>
#include <string>

using namespace std;

int check_dots(string inp, int i, int n) {
	while (i < n && inp[i] == '.') {
		i++;
	}
	return i;
}

int check_snake(string inp, int i, int n) {
	if (i < n) {
		if (inp[i] != 'H') {
			return -1;
		}
		i = check_dots(inp, i+1, n);
		if (inp[i] != 'T') {
			return -1;
		}
		return i+1;
	}
	return i;
}

int main(int argc, char const *argv[])
{
	int l, r, i, flag, n;
	string inp;
	cin >> l;
	while (l--) {
		cin >> r;
		cin >> inp;
		i = flag = 0;
		n = inp.length();
		while (i < n && i != -1) {
			i = check_dots(inp, i, n);
			// cout << "i: " << i << endl;
			i = check_snake(inp, i, n);
			// cout << "i: " << i << endl;
		}
		if (i == n) {
			cout << "Valid" << endl;
		} else {
			cout << "Invalid" << endl;
		}
	}
	return 0;
}