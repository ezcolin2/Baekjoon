#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int arr[100001];
	int dp[100001];
	int n;
	int res = -1001;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> arr[i];
	}
	dp[1] = arr[1];
	res = dp[1];
	for (int i = 2; i <= n; i++)
	{
		dp[i] = max(dp[i - 1] + arr[i], arr[i]);
		res = max(res, dp[i]);
	}
	cout << res;
}