#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	int num = 2 * n;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 0; j < i; j++)
		{
			cout << "*";
		}
		for (int j = 0; j < num - 2 * i;j++)
		{
			cout << " ";
		}
		for (int j = 0; j < i; j++)
		{
			cout << "*";
		}
		cout << '\n';
	}
	for (int i = n-1; i >= 1; i--)
	{
		for (int j = 0; j < i; j++)
		{
			cout << "*";
		}
		for (int j = 0; j < 2*(n-i); j++)
		{
			cout << " ";
		}
		for (int j = 0; j < i; j++)
		{
			cout << "*";
		}
		cout << '\n';
	}
}