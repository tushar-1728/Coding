#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, a, b, i, flag;
	cin >> t;
	while(t--) {
		cin >> a >> b;
		flag = i = 1;
		while (flag == 1) {
			if (a < i && flag == 1) {
				cout << "Bob" << endl;
				flag = 0;
			}
			a -= i++;

			if (b < i && flag == 1) {
				cout << "Limak" << endl;
				flag = 0;
			}
			b -= i++;
		}

	}
	return 0;
}