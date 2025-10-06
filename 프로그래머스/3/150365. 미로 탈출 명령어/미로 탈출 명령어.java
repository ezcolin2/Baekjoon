import java.util.*;

class Solution {
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        return bfs(n, m, x, y, r, c, k);
    }
    
    // start에 end까지 k 이동거리로 이동할 때 사전 순으로 가장 빠른 경로 반환
    private String bfs(int n, int m, int startX, int startY, int endX, int endY, int k){
		char[][][] dp = new char[n+1][m+1][k+1];
        boolean[][][] visited = new boolean[n+1][m+1][k+1];
        int[][][][] previousLocations = new int[n+1][m+1][k+1][2];
        // 하좌우상
        int[] dx = {1, 0, 0, -1};
        int[] dy = {0, -1, 1, 0};
        Map<Integer, Character> directionMap = new HashMap();
        directionMap.put(0, 'd');
        directionMap.put(1, 'l');
        directionMap.put(2, 'r');
        directionMap.put(3, 'u');
        
        Queue<int[]> queue = new LinkedList();
        visited[startX][startY][0] = true;
        queue.add(new int[]{startX, startY, 0});
        
        // 시작
        while (!queue.isEmpty()){
            int[] currentLocation = queue.remove();
            int cx = currentLocation[0];
            int cy = currentLocation[1];
            int cd = currentLocation[2];
            
            // 4방향 탐색
            for (int i=0; i<4; i++){
                int nx = cx+dx[i];
                int ny = cy+dy[i];
                int nd = cd+1;
                
                // 범위 벗어나면 스킵
                if (nx<1 || nx>n || ny<1 ||ny>m || nd>k){
                    continue;
                }
                
                // 방문했으면 스킵
                if (visited[nx][ny][nd]){
                    continue;
                }
                
                // 방문
                queue.add(new int[]{nx, ny, nd});
                visited[nx][ny][nd] = true;
                dp[nx][ny][nd] = directionMap.get(i);
                previousLocations[nx][ny][nd][0] = cx;
                previousLocations[nx][ny][nd][1] = cy;
            }
        }
        if (!visited[endX][endY][k]){
            return "impossible";
        }
        
        // 거꾸로 돌려서 지나온 경로를 구한다.
        StringBuffer sb = new StringBuffer();
        int cx = endX;
        int cy = endY;
        int cd = k;
        
        while (cx!=startX || cy!=startY || cd>0){
            sb.append(dp[cx][cy][cd]);
            int x = previousLocations[cx][cy][cd][0];
            int y = previousLocations[cx][cy][cd][1];
            cx =x;
            cy =y;
            cd--;
        }
        return sb.reverse().toString();
        
        //return dp[endX][endY][k] != null ? dp[endX][endY][k] : "impossible";
    }
}