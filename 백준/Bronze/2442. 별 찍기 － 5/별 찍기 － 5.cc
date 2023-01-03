#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	int num = 1;
	while (--n >= 0)
	{
		for (int i = 0; i < n; i++)
		{
			cout << " ";
		}
		for (int i = 0; i < num; i++)
		{
			cout << "*";
		}
		num += 2;
		cout << "\n";
	}
}