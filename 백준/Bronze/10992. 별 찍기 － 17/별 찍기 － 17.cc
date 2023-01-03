#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	int num = n;
	while (--num > 0)
	{
		for (int i = 0; i < num; i++)
		{
			cout << " ";
		}
		cout << "*";
		for (int i = 0; i < 2 * (n - num)-3; i++)
		{
			cout << " ";
		}
		if(n-num!=1)
			cout << "*";
		cout << '\n';
	}
	for (int i = 0; i < 2*n-1; i++)
	{
		cout << "*";
	}
}