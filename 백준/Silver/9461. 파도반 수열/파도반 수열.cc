#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
int main()
{
	int t;
	int n;
	ll dp[101];
	dp[1] = 1;
	dp[2] = 1;
	dp[3] = 1;
	dp[4] = 2;
	dp[5] = 2;
	int i = 6;
	cin >> t;
	while (t-- > 0)
	{
		cin >> n;
		for (; i <= n; i++)
		{
			dp[i] = dp[i - 1] + dp[i - 5];
		}
		cout << dp[n]<<'\n';
	}
}