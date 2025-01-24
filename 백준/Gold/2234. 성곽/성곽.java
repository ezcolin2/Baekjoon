import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    // 남동북서
    private static int[] dx = {1, 0, -1, 0};
    private static int[] dy = {0, 1, 0, -1};
    private static String[][] tower; // 성곽 정보
    private static int[][] rooms; // 각 좌표마다 방 번호 붙임
    private static int[] roomArea;
    private static int roomCnt;
    private static class Location{
        int x, y;
        public Location(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    /**
     *
     * @param integer 정수 (0~15)
     * @return 정수를 이진수로 변환한 뒤 string으로 반환 (15 -> "1111")
     */
    private static String changeIntegerToBinaryString(int integer){
         String res = "";
         while(integer > 0){
             res = integer%2+res;
             integer/=2;
         }
         // 0으로 패딩 채워주기
         while (res.length() < 4){
             res = '0'+res;
         }
         return res;
    }

    /**
     * 시작 좌표에서 bfs 탐색 후 방 번호를 붙인다.
     * @param roomNumber 방 번호
     * @param startX 시작 행
     * @param startY 시작 열
     */
    private static void bfs(int roomNumber, int startX, int startY){
        int n = tower.length;
        int m = tower[0].length;
        // 초기 값 세팅
        Queue<Location> queue = new LinkedList<>();
        queue.add(new Location(startX, startY));
        rooms[startX][startY] = roomNumber;

        // 큐가 빌 때까지
        while (!queue.isEmpty()){
            Location location = queue.remove();
            int x = location.x;
            int y = location.y;

            // 4 방향 탐색
            for (int i=0; i<4; i++){
                int nx = x+dx[i];
                int ny = y+dy[i];
                // 좌표 벗어나면 스킵
                if (nx<0 || nx>=n || ny<0 || ny>=m){
                    continue;
                }

                // 이미 방 번호가 부여되었으면 스킵
                if (rooms[nx][ny] != 0){
                    continue;
                }

                // 벽으로 가로막혀 있으면 스킵
                if (tower[x][y].charAt(i) == '1'){
                    continue;
                }

                // 방문
                rooms[nx][ny] = roomNumber;
                queue.add(new Location(nx, ny));
                roomArea[roomNumber]++;
            }
        }
    }

    /**
     * 방마다 방 번호를 부여
     */
    private static void allocateRoomNumber(){
        int n = tower.length; // 행 수
        int m = tower[0].length; // 열 수

        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                // 방 번호가 부여되지 않았다면 bfs로 탐색하여 부여
                if (rooms[i][j] != 0){
                    continue;
                }
                roomCnt+=1;
                bfs(roomCnt, i, j);
            }
        }
    }

    /**
     * 방 별로 연결된 방의 번호를 인접리스트로 반환
     * @return 연결된 방 번호 인접리싀트
     */
    private static Set<Integer>[] getLinkedRoomList(){
        int n = tower.length;
        int m = tower[0].length;
        Set<Integer>[] graph = new HashSet[n*m+1];
        for (int i=0; i<n*m+1; i++){
            graph[i] = new HashSet<>();
        }
        for (int x=0; x<n; x++){
            for (int y=0; y<m; y++){
                // 4 방향 탐색
                for (int i=0; i<4; i++){
                    int nx = x+dx[i];
                    int ny = y+dy[i];
                    // 좌표 벗어나면 스킵
                    if (nx<0 || nx>=n || ny<0 || ny>=m){
                        continue;
                    }
                    graph[rooms[x][y]].add(rooms[nx][ny]);
                    graph[rooms[nx][ny]].add(rooms[x][y]);
                }
            }
        }
        return graph;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        tower = new String[n][m]; // 성곽 초기화
        rooms = new int[n][m]; // 방 번호 초기화
        roomArea = new int[n*m+1]; // 방마다 넓이 초기화
        for (int i=0; i<n*m+1; i++){
            roomArea[i] = 1;
        }
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++){
                tower[i][j] = changeIntegerToBinaryString(Integer.parseInt(st.nextToken()));
            }
        }

        // 연결된 방의 번호들을 구한다.
        allocateRoomNumber();
        Set<Integer>[] linkedList = getLinkedRoomList();

        // 연결된 방 두 개를 연결했을 때 최대 방 개수를 구한다.
        int res = 0;
        for (int i=1; i<=roomCnt; i++){
            for (Integer roomNumber: linkedList[i]){
                // 같은 방이라면 스킵
                if (i == roomNumber){
                    continue;
                }
                res = Math.max(res, roomArea[i]+roomArea[roomNumber]);
            }
        }
        // 가장 넓은 방의 넓이
        int maxArea = 0;
        for (int i=0; i<roomArea.length; i++){
            maxArea = Math.max(maxArea, roomArea[i]);
        }
        System.out.println(roomCnt);
        System.out.println(maxArea);
        System.out.println(res);
    }
}