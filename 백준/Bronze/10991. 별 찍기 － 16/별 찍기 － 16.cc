#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	int num = n;
	while (--num >= 0)
	{
		for (int i = 0; i < num; i++)
		{
			cout << " ";
		}
		for (int i = 0; i < n - num; i++)
		{
			cout << "* ";
		}
		cout << '\n';
	}
}