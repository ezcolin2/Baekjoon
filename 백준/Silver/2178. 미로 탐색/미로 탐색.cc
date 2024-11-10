#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;
#define MAX 100
int n, m;
int maze[MAX][MAX];
bool visit[MAX][MAX];
int X[4] = { 0,1,0,-1 };
int Y[4] = { 1,0,-1,0 };
queue<pair<int, int>> q;
bool inrange(int x, int y) {
	return (x >= 0 && y >= 0 && x < m && y < n);
}
void BFS(int x, int y) {
	q.push({ x,y });
	visit[x][y] = true;
	while (!q.empty()) {
		pair<int, int> temp = q.front();
		q.pop();
		int xx, yy;
		for (int i = 0; i < 4; i++) {
			xx = temp.first + X[i];
			yy = temp.second + Y[i];
			if (inrange(xx, yy) && maze[xx][yy] != 0 && !visit[xx][yy]) {
				q.push({ xx,yy });
				visit[xx][yy] = true;
				maze[xx][yy] = maze[temp.first][temp.second] + 1;
			}
		}
	}
}
int main()
{
	string s;
	cin >> m >> n;
	for (int i = 0; i < m; i++) {
		cin >> s;
		for (int j = 0; j < n; j++) {
			maze[i][j] = s[j] - '0';
		}
	}
	BFS(0, 0);
	cout << maze[m - 1][n - 1];
}