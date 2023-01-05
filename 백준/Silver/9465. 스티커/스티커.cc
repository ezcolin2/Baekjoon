#include <iostream>
#include <algorithm>
using namespace std;
int main() 
{
	int arr[2][100000];
	int n,t;
	cin >> t;
	while (t-- > 0)
	{
		cin >> n;

		for (int i = 0; i < 2; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cin >> arr[i][j];
			}
		}
		if (n == 1)
		{
			cout << max(arr[0][0], arr[1][0])<<'\n';
			continue;
		}
		arr[0][1] += arr[1][0];
		arr[1][1] += arr[0][0];
		for (int i = 2; i < n; i++)
		{
			arr[0][i] += max(arr[1][i - 1], arr[1][i - 2]);
			arr[1][i] += max(arr[0][i - 1], arr[0][i - 2]);
		}
		cout << max(arr[0][n - 1], arr[1][n - 1])<<'\n';
	}
}