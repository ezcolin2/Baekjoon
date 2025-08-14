import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.BufferedWriter;
import java.util.StringTokenizer;

/**
 * 구슬의 다음 위치를 구하는 방법
 * 1. 벽만 존재하는 보드를 만들어서 기울이고 난 뒤 구슬의 위치를 가져온다. (그 후 초기화)
 * 2. 움직이기 전에 구슬을 쌓기 시작할 시작점을 구한다. (#R..#.#) 이 보드를 오른쪽으로 기울이면 중간부터 쌓여야 한다.
 * 3. 움직이기 전에 탐색으로 구멍에 들어갈 수 있는지 확인한다.
 * 4. (##RB..#) 이 보드를 오른쪽으로 기울이면 RB 순서가 유지되어야 한다.
 * 5. 벽은 그 이전 위치로, 공은 그 위치로 이동해야 한다.
 * 
 * 구슬 순서 유지하기
 * 1. 기울이는 방향으로 탐색을 진행하면서 만약 다른 공을 만났다면 어떠한 공이 앞에 있는지 플래그를 설정한다.
 * 2. 두 구슬 모두 충돌이 없다고 가정하고 위치를 구한다.
 * 3. 위치가 동일하다면 플래그를 기반으로 뒤에 있는 공을 옮긴다.
 * 
 * 
 * 시간 복잡도를 줄이기
 * 1. 매번 새로운 배열을 만들지 않고 기존 배열을 재활용한다.
 * 2. 움직이는 물체는 오직 두 개이기 때문에 기울일 때 해당 두 물체 위치를 기반으로 해당하는 행 또는 열만 움직인다.
 * 
 * 전체적인 구현 방식
 * 1. 백트래킹으로 4^10 모든 경우의 수를 구한다.
 */
public class Main {
    // 동서남북
    private static int[] dx = { 0, 0, 1, -1 };
    private static int[] dy = { 1, -1, 0, 0 };
    private static Location redLocation;
    private static Location blueLocation;
    private static Location goalLocation;
    private static char[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        board = new char[n][m];
        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = row.charAt(j);
                switch (board[i][j]) {
                    case 'B':
                        blueLocation = new Location(i, j);
                        break;
                    case 'R':
                        redLocation = new Location(i, j);
                        break;
                    case 'O':
                        goalLocation = new Location(i, j);
                        break;
                }
            }
        }
        // // Location hello = getNextLocation(redLocation, blueLocation, 1)[0];
        // // System.out.println(hello.x);
        // // System.out.println(hello.y);
        // return;
        int result = backTracking(redLocation, blueLocation, 1);
        bw.write(String.valueOf(result == Integer.MAX_VALUE ? -1 : result));
        bw.close();
    }

    private static int backTracking(Location redLocation, Location blueLocation, int cnt) {
        if (cnt == 11) {
            return Integer.MAX_VALUE;
        }
        int minValue = Integer.MAX_VALUE;
        // 4방향
        for (int i = 0; i < 4; i++) {
            Location[] locationList = getNextLocation(redLocation, blueLocation, i);
            Location nextRedLocation = locationList[0];
            Location nextBlueLocation = locationList[1];
            // 파란 공이 들어갔다면
            if (nextBlueLocation.x == goalLocation.x && nextBlueLocation.y == goalLocation.y) {
                minValue = Math.min(minValue, Integer.MAX_VALUE);
            }
            // 만약 파란 공이 안 들어가고 빨간 공이 들어갔다면
            else if (nextRedLocation.x == goalLocation.x && nextRedLocation.y == goalLocation.y) {
                minValue = Math.min(minValue, cnt);
            }

            // 둘 다 안들어갔다면
            minValue = Math.min(minValue, backTracking(nextRedLocation, nextBlueLocation, cnt + 1));
        }
        return minValue;
    }

    private static Location[] getNextLocation(Location redLocation, Location blueLocation, int direction) {
        boolean isRedAhead = false; // 빨간 공이 앞에 있는지
        boolean isBlueAhead = false; // 파란 공이 앞에 있는지
        Location currentRedLocation = new Location(redLocation.x, redLocation.y);
        Location currentBlueLocation = new Location(blueLocation.x, blueLocation.y);
        Location nextRedLocation;
        Location nextBlueLocation;
        // 빨간 공부터
        while (!(currentRedLocation.x == goalLocation.x && currentRedLocation.y == goalLocation.y)) {
            nextRedLocation = new Location(currentRedLocation.x + dx[direction], currentRedLocation.y + dy[direction]);
            // 만약 파란 공을 만나면
            if (nextRedLocation.x == blueLocation.x && nextRedLocation.y == blueLocation.y) {
                isBlueAhead = true;
                currentRedLocation.x = nextRedLocation.x;
                currentRedLocation.y = nextRedLocation.y;
            }
            // 골인 지점을 만나면
            if (nextRedLocation.x == goalLocation.x && nextRedLocation.y == goalLocation.y) {
                currentRedLocation.x = nextRedLocation.x;
                currentRedLocation.y = nextRedLocation.y;
                break;
            }

            // 벽을 만나면
            if (board[nextRedLocation.x][nextRedLocation.y] == '#') {
                // 갱신 X
                break;
            }
            currentRedLocation.x = nextRedLocation.x;
            currentRedLocation.y = nextRedLocation.y;
        }
        // 파란 공
        while (!(currentBlueLocation.x == goalLocation.x && currentBlueLocation.y == goalLocation.y)) {
            nextBlueLocation = new Location(currentBlueLocation.x + dx[direction],
                    currentBlueLocation.y + dy[direction]);
            // 만약 빨간 공을 만나면
            if (nextBlueLocation.x == redLocation.x && nextBlueLocation.y == redLocation.y) {
                isRedAhead = true;
                currentBlueLocation.x = nextBlueLocation.x;
                currentBlueLocation.y = nextBlueLocation.y;
            }
            // 골인 지점을 만나면
            if (nextBlueLocation.x == goalLocation.x && nextBlueLocation.y == goalLocation.y) {
                currentBlueLocation.x = nextBlueLocation.x;
                currentBlueLocation.y = nextBlueLocation.y;
                break;
            }

            // 벽을 만나면
            if (board[nextBlueLocation.x][nextBlueLocation.y] == '#') {
                // 갱신 X
                break;
            }
            currentBlueLocation.x = nextBlueLocation.x;
            currentBlueLocation.y = nextBlueLocation.y;
        }

        // 파란 공이 앞에 있으면 빨간 공은 한 칸 뒤로
        if (!(currentRedLocation.x == goalLocation.x && currentRedLocation.y == goalLocation.y) && isBlueAhead) {
            int oppositeDirection = -1;
            switch (direction) {
                case 0:
                    oppositeDirection = 1;
                    break;
                case 1:
                    oppositeDirection = 0;
                    break;
                case 2:
                    oppositeDirection = 3;
                    break;
                case 3:
                    oppositeDirection = 2;
                    break;
            }
            currentRedLocation.x += dx[oppositeDirection];
            currentRedLocation.y += dy[oppositeDirection];
        }
        // 빨간 공이 앞에 있으면 파란 공은 한 칸 뒤로
        if (!(currentBlueLocation.x == goalLocation.x && currentBlueLocation.y == goalLocation.y) && isRedAhead) {
            int oppositeDirection = -1;
            switch (direction) {
                case 0:
                    oppositeDirection = 1;
                    break;
                case 1:
                    oppositeDirection = 0;
                    break;
                case 2:
                    oppositeDirection = 3;
                    break;
                case 3:
                    oppositeDirection = 2;
                    break;
            }
            currentBlueLocation.x += dx[oppositeDirection];
            currentBlueLocation.y += dy[oppositeDirection];
        }
        return new Location[] { currentRedLocation, currentBlueLocation };
    }

    static class Location {
        int x;
        int y;

        public Location(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
