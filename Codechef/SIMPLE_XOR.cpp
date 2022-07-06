#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int t, l, r, flag;
	cin >> t;
	while (t--) {
		cin >> l >> r;
		flag = 1;
		for (int m = l; m <= r && flag; ++m)
		{
			for (int n = m+1; n <= r && flag; ++n)
			{
				for (int o = n+1; o <= r && flag; ++o)
				{
					for (int p = o+1; p <= r && flag; ++p)
					{
						if (m^n^o^p == 0) {
							printf("%d %d %d %d\n", m, n, o, p);
							flag = 0;
						}
					}
				}
			}
		}
		if (flag)
			printf("-1\n");
	}
	return 0;
}