#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int* arr = new int[1000001];
	arr[1] = 0;
	int n;
	cin >> n;
	for (int i = 2; i <= n; i++)
	{
		arr[i] = arr[i - 1] + 1;
		if (i % 3 == 0)
			arr[i] = min(arr[i / 3 ]+ 1, arr[i]);
		if (i % 2 == 0)
			arr[i] = min(arr[i / 2] + 1, arr[i]);
	}
	cout << arr[n];
}