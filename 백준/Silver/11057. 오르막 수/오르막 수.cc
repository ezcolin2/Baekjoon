#include <iostream>
using namespace std;
int main() 
{
	int arr[1001][10] = { 0, };
	int n;
	for (int i = 0; i < 10; i++)
	{
		arr[1][i] = 1;
	}
	cin >> n;
	for (int i = 2; i <= n; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			for (int k = 0; k <= j; k++)
			{
				arr[i][j] += arr[i-1][k]%10007;
			}
		}
	}
	int res = 0;
	for (int i = 0; i < 10; i++)
	{
		res += arr[n][i];
	}
	cout << res % 10007;
}