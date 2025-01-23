import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    // 동서남북
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    private static class Node{
        int x;
        int y;
        public Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    // 중력 함수
    // 시간 복잡도: O(N*M)
    private static char[][] gravity(char[][] field){
        int n = field.length;
        int m = field[0].length;
        // 복사하기
        // O(N*M)
        char[][] newField = new char[n][m];
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                newField[i][j] = '.';
            }
        }

        // 중력이 작용한 이후 새로운 필드를 만든다.
        // O(N*M)
        // 각 열마다
        for (int i=0; i<m ;i++){
            // 내려갈 위치
            int currentIndex = n-1;
            // 아래에서부터 탐색
            for (int j=n-1; j>=0; j--){
                // 뿌요라면 내린다.
                if (field[j][i] != '.'){
                    newField[currentIndex][i] = field[j][i];
                    // 이미 쌓였으니까 다음 내려갈 위치를 올린다.
                    currentIndex-=1;
                }
            }
        }

        return newField;
    }

    // field[startX][startY]부터 시작해서 연결된 모든 같은 뿌요를 제거한다.
    // visited는 전체적으로 사용하는 방문 배열이고
    // tempVisited는 현재 시점 방문 배열이다.
    // 터뜨렸는지 반환
    private static boolean bomb(char[][] field, boolean[][] visited, int startX, int startY){
        // 시작 뿌요
        char startPuyo = field[startX][startY];
        int n = field.length;
        int m = field[0].length;

        // 복사하기
        // O(N*M)
        char[][] newField = Arrays.stream(field).map(
                row -> row.clone()
        ).toArray(char[][]::new);

        // 방문 배열
        // O(N*M)
        boolean[][] tempVisited = new boolean[n][m];

        // 큐
        Queue<Node> queue = new LinkedList<>();


        // 시작 점 큐에 넣기
        queue.add(new Node(startX, startY));
        tempVisited[startX][startY] = true;
        visited[startX][startY] = true;

        // 연결된 뿌요 개수
        int connectedPuyo = 1;

        // 큐가 빌 때까지
        while(!queue.isEmpty()){
            // 꺼낸다.
            Node currentNode = queue.remove();
            int x = currentNode.x;
            int y = currentNode.y;

            // 4방향 탐색
            for (int i=0; i<4; i++){
                int nx = x+dx[i];
                int ny = y+dy[i];

                // 좌표를 벗어났다면 스킵
                if (nx<0 || nx>=n || ny<0 || ny>=m){
                    continue;
                }

                // 방문했다면 스킵
                if (tempVisited[nx][ny]){
                    continue;
                }

                // 같은 뿌요가 아니라면 스킵
                if (field[nx][ny] != startPuyo){
                    continue;
                }

                // 방문
                queue.add(new Node(nx, ny));
                tempVisited[nx][ny] = true;
                visited[startX][startY] = true;
                connectedPuyo++;
            }
        }

        // 연결된 뿌요가 4개 이상이면 모두 터뜨린다.
        if (connectedPuyo < 4){
            return false;
        }

        for (int i=0; i<n ;i++){
            for (int j=0; j<m ;j++){
                if (tempVisited[i][j]){
                    field[i][j] = '.';
                }
            }
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        // 필드
        char [][] field = new char[12][6];

        // 방문 여부
        boolean[][] visited = new boolean[12][6];

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 필드 뿌요로 초기화
        for (int i=0; i<12; i++){
            st = new StringTokenizer(br.readLine());
            String temp = st.nextToken();

            for (int j=0; j<6; j++){
                field[i][j] = temp.charAt(j);
            }

        }

        // 게임 시작
        // 가장 먼저 중력을 적용한다.
        field = gravity(field);

        // 횟수
        int res = 0;

        // 넉넉하게 100번 정도 수행한다.
        // 총 필드 개수가 72번이니 충분
        for (int i=0; i<100; i++){
            // 시작할 때 visited 초기화
            for (int j=0; j<12; j++){
                for (int k=0; k<6; k++){
                    visited[j][k] = false;
                }
            }
            // 한 번 시작할 때 터뜨린 횟수
            int tempCnt = 0;
            for (int j=0; j<12; j++){
                for (int k=0; k<6; k++){
                    // 이미 방문했다면 스킵
                    if (visited[j][k]){
                        continue;
                    }

                    // 뿌요가 아니면 스킵
                    if (field[j][k] == '.'){
                        continue;
                    }

                    if (bomb(field, visited, j, k)){
                        tempCnt++;
                    }
                }
            }
            // 한 번 끝났을 때 터뜨린 게 있다면 연쇄 증가
            if (tempCnt >= 1){
                field = gravity(field);
                res++;
            } else{
                break;
            }

        }
        System.out.println(res);
    }
}