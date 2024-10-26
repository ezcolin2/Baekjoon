#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
int n, m;
ll arr[500000];
int lower_binary(ll left,ll right,ll num) {
	while (left < right) {
		ll mid = (left + right) / 2;
		if (arr[mid] >= num) {
			right = mid;
		}
		else left = mid + 1;
	}
	return right;
}
int upper_binary(ll left, ll right, ll num) {
	while (left < right) {
		ll mid = (left + right) / 2;
		if (arr[mid] <= num) {
			left= mid+1;
		}
		else right = mid;
	}
	return left;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	ll arr2[500000];
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n);
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> arr2[i];
	}
	for (int i = 0; i < m; i++) {
		int low = lower_binary(0, n - 1, arr2[i]);
		int up = upper_binary(0, n - 1, arr2[i]);

		if (up == n - 1 && arr2[i] == arr[up])up++;
		cout << up -low << ' ';

	}
}