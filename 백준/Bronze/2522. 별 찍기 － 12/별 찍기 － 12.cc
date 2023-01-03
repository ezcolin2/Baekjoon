#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int n;
	cin >> n;
	int num = n;
	while (--n > -num)
	{
		
		for (int i = 0; i < abs(n); i++)
		{
			cout << " ";
		}
		for (int i = 0; i < num-abs(n); i++)
		{
			cout << "*";
		}
		cout << '\n';
	}
}