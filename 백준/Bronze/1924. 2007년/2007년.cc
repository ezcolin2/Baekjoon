#include <iostream>
#include <string>
using namespace std;
int main() {
	string day[7] = { "MON","TUE","WED","THU","FRI","SAT","SUN" };
	int month[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
	int x, y;
	cin >> x >> y;
	int distance = 0;
	for (int i = 1; i < x; i++)
	{
		distance += month[i -1];
	}
	distance += y - 1;
	cout << day[distance % 7];
}