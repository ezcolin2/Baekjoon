#include <iostream>
#include <algorithm>
using namespace std;
int main() 
{
	int n;
	int arr[1001];
	int asc[1001];
	fill_n(asc, 1001, 1);
	int res = 0;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> arr[i];
	}
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			if (arr[j] < arr[i])
				asc[i] = max(asc[i],asc[j]+1);
		}
		res = max(res, asc[i]);
	}
	cout << res;
}