import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char[][] arr = new char[5][5];
        for (int i=0; i<5; i++){
            String s = br.readLine();
            for (int j=0; j<5; j++){
                arr[i][j] = s.charAt(j);
            }
        }
        Combination combination = new Combination(arr);
        combination.choose(0, 0, 0);
        bw.write(String.valueOf(combination.numberOfCases));
        bw.close();
    }
}
class Combination{
    public LinkedList<Coordinate> combination;
    public char[][] arr;
    // 동서남북
    public int[] dx = {0, 0, 1, -1};
    public int[] dy = {1, -1, 0, 0};
    public int numberOfCases = 0;
    Combination(char[][] arr){
        this.combination = new LinkedList();
        this.arr = arr;
    }
    public void choose(int x, int y, int cnt){
        // 끝까지 조사했다면
        if (x==5){
            // 7개 모두 선택했다면
            if (cnt==7){
                // 조건을 모두 만족한다면
                if (isGreaterThanFour() && isConnected()){
                    this.numberOfCases++;
                }
            }
            return;
        }
        // x, y를 선택
        this.combination.add(new Coordinate(x, y));
        int nx = x;
        int ny = y+1;
        if (ny == 5){
            nx++;
            ny=0;
        }        
        choose(nx, ny, cnt+1);
        this.combination.removeLast();
        
        // x, y를 선택하지 않음
        choose(nx, ny, cnt);
    }
    /**
        이다솜파 학생이 4명 이상인지
    */
    public boolean isGreaterThanFour(){
        // 현재 조합에서 이다솜파 학생의 개수를 구한다.
        int cnt = 0;
        for (Coordinate coordinate: combination){
            if (this.arr[coordinate.x][coordinate.y] == 'S'){
                cnt++;
            }
        }
        if (cnt>=4){
            return true;
        }
        return false;
    }
    
    /**
        현재 combination의 좌표들이 전부 연결되어 있는지
    */
    public boolean isConnected(){
        // 방문 여부 배열
        boolean[][] visited = new boolean[5][5];
        
        // 방문 가능 배열
        boolean[][] canVisit = new boolean[5][5];
        for (Coordinate coordinate: combination){
            canVisit[coordinate.x][coordinate.y] = true;
        }
        
        // 큐
        Queue<Coordinate> queue = new LinkedList();
        
        // 처음 좌표 넣기
        Coordinate firstCoordinate = this.combination.get(0);
        queue.add(firstCoordinate);
        visited[firstCoordinate.x][firstCoordinate.y] = true;
        
        // 큐가 빌 때까지
        while (!queue.isEmpty()){
            // 꺼내오기
            Coordinate currentCoordinate = queue.remove();
            int cx = currentCoordinate.x;
            int cy = currentCoordinate.y;
            // 4방향 탐색
            for (int i=0; i<4; i++){
                int nx = cx+dx[i];
                int ny = cy+dy[i];
                // 범위 벗어나면 스킵
                if (nx<0 || nx>4 || ny<0 || ny>4){
                    continue;
                }
                // 방문했으면 스킵 
                if (visited[nx][ny]){
                    continue;
                }
                // 방문할 수 없다면 스킵
                if (!canVisit[nx][ny]){
                    continue;
                }
                // 방문하기
                queue.add(new Coordinate(nx, ny));
                visited[nx][ny] = true;
            }
        }
        // 조합 내 모든 좌표를 순회
        for (Coordinate coordinate: combination){
            if (!(visited[coordinate.x][coordinate.y] && canVisit[coordinate.x][coordinate.y])){
                return false;
            }
        }
        return true;
    }
}
class Coordinate{
    public int x;
    public int y;
    Coordinate(int x, int y){
        this.x = x;
        this.y = y;
    }
}