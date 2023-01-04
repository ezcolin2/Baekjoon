#include <iostream>
using namespace std;
int main() 
{
	int arr[1001];
	arr[1] = 1;
	arr[2] = 2;
	int n;
	cin >> n;
	for (int i = 3; i <= n; i++)
	{
		arr[i] = (arr[i - 1] + arr[i - 2])%10007;
	}
	cout << arr[n];
}