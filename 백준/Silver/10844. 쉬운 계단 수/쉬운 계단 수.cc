#include <iostream>
using namespace std;
int main() 
{
	long long arr[101][10];
	arr[1][0] = 0;
	for (int i = 1; i < 10; i++)
	{
		arr[1][i] = 1;
	}
	int n;
	long long res = 0;
	cin >> n;
	for (int i = 2; i <= n; i++)
	{
		arr[i][0] = arr[i - 1][1]%1000000000;
		for (int j = 1; j < 9; j++)
		{
			arr[i][j] = (arr[i - 1][j - 1] + arr[i - 1][j + 1])%1000000000;
		}
		arr[i][9] = arr[i-1][8]%1000000000;
	}
	for (int i = 0; i < 10; i++)
	{
		res += arr[n][i];
	}
	cout << res%1000000000;
}