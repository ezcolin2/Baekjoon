#include <iostream>
#include <algorithm>
using namespace std;
int main() 
{
	int arr[1001];
	arr[0] = 0;
	int dp[1001] = { 0, };
	int n;
	int Max=0;
	int res = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	for (int i = 0; i < n; i++)
	{
		Max = 0;
		for (int j = arr[i]-1; j >= 0; j--)
		{
			Max = max(dp[j], Max);
		}
		dp[arr[i]] = Max + arr[i];
		res = max(res, dp[arr[i]]);
	}
	cout << res;
}
