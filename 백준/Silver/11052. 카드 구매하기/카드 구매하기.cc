#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int arr[1001];
	int dp[1001];
	dp[0] = 0;
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
		dp[i] = arr[i];
		for (int j = 1; j <= i/2; j++) {
			dp[i] = max(dp[i], dp[j] + dp[i-j]);
		}
	}
	cout << dp[n];
}