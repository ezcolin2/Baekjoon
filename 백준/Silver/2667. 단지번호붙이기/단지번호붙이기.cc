#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
#define MAX 25
int n, cnt;
string house[MAX];
bool visit[MAX][MAX];
int arr[MAX * MAX];
int X[4] = { 1,0,-1,0 };
int Y[4] = { 0,1,0,-1 };
void DFS(int x, int y) {
	visit[x][y] = true;
	cnt++;
	int xx, yy;
	for (int i = 0; i < 4; i++) {
		xx = x + X[i];
		yy = y + Y[i];
		if (xx >= 0 && xx < n && yy >= 0 && yy < n && !visit[xx][yy] && house[xx][yy] == '1')
			DFS(xx, yy);
	}
}
int main()
{
	cnt = 0;
	int num = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> house[i];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			visit[i][j] = false;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visit[i][j] && house[i][j] == '1') {
				DFS(i, j);
				arr[num++] = cnt;
				cnt = 0;
			}
		}
	}
	sort(arr, arr + num);
	cout << num << '\n';
	for (int i = 0; i < num; i++) {
		cout << arr[i] << '\n';
	}
}