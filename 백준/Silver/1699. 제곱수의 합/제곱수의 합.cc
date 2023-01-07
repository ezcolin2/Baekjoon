#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int dp[100001] = { 0, };
	dp[1] = 1;
	int n;
	cin >> n;
	int i = 1;
	for (int k = 1; k <= n; k++)
	{
		for (; i * i < k; i++);
		if (i * i == k)
		{
			dp[k] = 1;
		}
		else
		{
			i--;
			dp[k] = dp[1] + dp[k - 1];
			for (int j = 2; j <= i; j++)
			{
				dp[k] = min(dp[j * j] + dp[k - j * j],dp[k]);
			}
		}
	}
	cout << dp[n];
}