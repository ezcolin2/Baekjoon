#include <iostream>
using namespace std;
typedef long long ll;
ll n, m ,res;
ll arr[1000000];
bool isok(ll h) {
	ll temp = 0;
	for (ll i = 0; i < n; i++) {
		if(arr[i]>=h)
			temp += arr[i] - h;
	}
	if (temp >= m) return true;
	else return false;
}
void binary(ll left, ll right) {
	if (left >= right) return;
	ll mid = (left + right)/2;
	if (isok(mid)) {
		if (res < mid) res = mid;
		binary(mid+1, right);
	}
	else {
		binary(left, mid);
	}
}
int main() {
	cin >> n >> m;
	res = 0;
	ll start = 0;
	for (ll i = 0; i < n; i++) {
		cin >> arr[i];
		if (arr[i] > start) start = arr[i];
	}
	binary(0, start);
	cout << res;
}