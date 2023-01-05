#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int dp[2][10001];
	dp[0][0] = 0;
	dp[1][0] = 0;
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> dp[0][i];
		dp[1][i] = dp[0][i];
	}
	dp[1][2] += dp[0][1];
	if (n == 1)
	{
		cout << max(dp[0][1], dp[1][1]);
		return 0;
	}
	for (int i = 3; i <= n; i++)
	{
		dp[0][i] += max(max(dp[0][i - 2], dp[1][i - 2]),dp[1][i-3]);
		dp[1][i] += dp[0][i - 1];
	}
	cout << max(max(dp[0][n - 1], dp[1][n - 1]), max(dp[0][n], dp[1][n]));
}