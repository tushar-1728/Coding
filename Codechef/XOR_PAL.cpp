#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, count;
	string inp, opt;
	cin >> t;
	while (t--)
	{
		cin >> n;
		cin >> inp;
		count = 0;
		for (int i = 0; i < n/2; ++i)
		{
			if (inp[i] != inp[n-i-1])
			{
				count++;
			}
		}
		
		cout << (count+1)/2 << endl;
	}
	return 0;
}