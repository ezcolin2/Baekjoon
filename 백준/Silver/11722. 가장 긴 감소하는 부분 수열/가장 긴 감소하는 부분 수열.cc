#include <iostream>
#include <algorithm>
using namespace std;
int main() 
{
	int arr2[1001];
	int arr[1001];
	int dp[1001] = { 0, };
	int n;
	int Max;
	int res=0;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> arr2[i];
		arr[n - 1 - i] = arr2[i];
	}
	
	for (int i = 0; i < n; i++)
	{
		Max = 0;
		for (int j = arr[i] - 1; j >= 1; j--)
		{
			Max = max(Max, dp[j]);
		}
		dp[arr[i]] = Max + 1;
		res = max(res, dp[arr[i]]);

	}
	cout << res;
}
