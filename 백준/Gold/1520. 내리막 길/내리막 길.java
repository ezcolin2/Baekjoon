import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main{
    // 동서남북
    public static int[] dx = {0, 0, 1, -1};
    public static int[] dy = {1, -1, 0, 0};
    public static int[][] map;
    public static int[][] arr;
    public static boolean[][] visited;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        arr = new int[n][m];
        visited = new boolean[n][m];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        arr[n-1][m-1] = 1;
        visited[n-1][m-1] = true;
        bw.write(String.valueOf(getTotalWayCount(0, 0)));
        bw.close();
    }

    public static int getTotalWayCount(int x, int y){
        if (x == map.length-1 && y == map[0].length-1){
            visited[x][y] = true;
            return arr[x][y];
        }
        // 4방향 탐색
        for (int i=0; i<4; i++){
            int nx = x+dx[i];
            int ny = y+dy[i];
            // 범위 넘어가면 스킵
            if (nx<0 || nx>=map.length || ny <0 || ny>=map[0].length){
                continue;
            }

            // 갈 수 없는 곳이면 스킵
            if (map[nx][ny] >= map[x][y]){
                continue;
            }

            // 방문을 했지만 아직 경로가 확정나지 않은 경우 스킵
            if (visited[nx][ny] && arr[nx][ny] == 0){
                continue;
            }

            // 방문을 했고 이미 경로가 확정난 경우
            if (visited[nx][ny] && arr[nx][ny] > 0){
                // 다시 방문할 필요가 없다.
                arr[x][y]+=arr[nx][ny];
                continue;
            }

            // 방문을 했고 경로가 아직 확정 안 났다면 방문
            visited[nx][ny] = true;
            arr[nx][ny] = getTotalWayCount(nx, ny);
            arr[x][y] += arr[nx][ny];
        }
        return arr[x][y];
    }


}