#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
#define MAX 51
int n,m;
int house[MAX][MAX];
bool visit[MAX][MAX];
void DFS(int x,int y) {
	visit[x][y] = true;
	for (int i = max(0, x - 1); i<min(x+2,n); i++) {
		for (int j = max(0, y - 1); j < min(y+2,m); j++) {
			if (!visit[i][j] && house[i][j] == 1) DFS(i, j);
		}
	}
}
int main()
{
	int cnt = 0;
	cin >> m>>n;
	while (n != 0 || m != 0) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> house[i][j];
				visit[i][j] = false;
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (!visit[i][j] && house[i][j] == 1) {
					DFS(i, j);
					cnt++;
				}
			}
		}
		cout << cnt << '\n';
		cnt = 0;
		cin >> m >> n;
	}
}