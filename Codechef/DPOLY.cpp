#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, count, temp;
	cin >> t;
	while (t--)
	{
		cin >> n;
		count = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> temp;
			if (temp != 0)
			{
				count = i > count ? i : count;
			}
		}
		cout << count << endl;
	}
	return 0;
}