#include <iostream>
#include <cmath>
using namespace std;
int main() {
	int n;
	cin >> n;
	if (n == 1)
	{
		return 0;
	}
	for (int i = 2; i <= n; i++)
	{
		if (n % i == 0)
		{
			while (n % i == 0)
			{
				n /= i;
				cout << i << endl;
			}
		}
	}
}