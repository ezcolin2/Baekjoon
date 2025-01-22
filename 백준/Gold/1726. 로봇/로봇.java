import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static class LocationInfo{
        public int x;
        public int y;
        public int direction;

        LocationInfo(int x, int y, int direction){
            this.x = x;
            this.y = y;
            this.direction = direction;
        }
    };
    // 동서남북
    private static int[] dx = {0, 0, 1, -1};
    private static int[] dy = {1, -1, 0, 0};
    private static int getMinCommand(int[][] arr, LocationInfo startLocation, LocationInfo endLocation){
        int n = arr.length;
        int m = arr[0].length;
        // 방문 정보 모두 false로 초기화
        boolean[][][] visited = new boolean[n][m][4];

        // 최단 거리
        int[][][] distance = new int[n][m][4];

        // 큐 생성
        Queue<LocationInfo> queue = new LinkedList<>();

        // 초기 값
        queue.add(startLocation);
        visited[startLocation.x][startLocation.y][startLocation.direction] = true;

        // 큐가 빌 때까지
        while (!queue.isEmpty()){
            LocationInfo currentLocation = queue.remove();
            int x = currentLocation.x;
            int y =currentLocation.y;
            int direction = currentLocation.direction;
            // 방향 돌림
            for (int i=1; i<4; i++){
                // 2로 나눈 몫이 같다면 한 번의 명령으로 이동 가능
                int nextDirection = (direction+i)%4;
                // 방문했다면 스킵
                if (visited[x][y][nextDirection]){
                    continue;
                }
                if (direction/2 != nextDirection/2){
                    distance[x][y][nextDirection] = distance[x][y][direction]+1;
                } else{
                    continue;
                }

                // 큐에 넣기
                visited[x][y][nextDirection] = true;
                queue.add(new LocationInfo(x, y, nextDirection));
            }

            // 해당 방향으로 이동
            for (int i=1; i<4; i++){
                int nx = x+(dx[direction]*i);
                int ny = y+(dy[direction]*i);
                // 범위 넘어가면 스킵
                if (nx<0 || nx>=n || ny<0 || ny>=m){
                    break;
                }
                // 궤도가 없으면 스킵
                if (arr[nx][ny] == 1){
                    break;
                }
                // 방문했다면 스킵
                if (visited[nx][ny][direction]){
                    continue;
                }
                // 큐에 넣기
                visited[nx][ny][direction] = true;
                distance[nx][ny][direction] = distance[x][y][direction]+1;
                queue.add(new LocationInfo(nx, ny, direction));

            }
        }
        return distance[endLocation.x][endLocation.y][endLocation.direction];

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // n, m
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 지도 정보
        int[][] arr = new int[n][m];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 시작, 도착 정보
        st = new StringTokenizer(br.readLine());
        int start_x = Integer.parseInt(st.nextToken())-1;
        int start_y = Integer.parseInt(st.nextToken())-1;
        int start_direction = Integer.parseInt(st.nextToken())-1;
        st = new StringTokenizer(br.readLine());
        int end_x = Integer.parseInt(st.nextToken())-1;
        int end_y = Integer.parseInt(st.nextToken())-1;
        int end_direction = Integer.parseInt(st.nextToken())-1;

        System.out.println(getMinCommand(
                arr,
                new LocationInfo(start_x, start_y, start_direction),
                new LocationInfo(end_x, end_y, end_direction)
        ));

    }
}