import java.util.Queue;
import java.util.LinkedList;
import java.util.Set;
import java.util.HashSet;
class Solution {
    private char[][] containerArr; // 컨테이너 배열
    private boolean[][] isExistContainer; // 컨테이너가 존재
    private int[] dx = {0, 0, 1, -1};
    private int[] dy = {1, -1, 0, 0};
    public int solution(String[] storage, String[] requests) {
        // 동서남북
        int n = storage.length;
        int m = storage[0].length();
        containerArr = new char[n][m];
        isExistContainer = new boolean[n][m];
        // 편의를 위해 char 2차원 배열로 변경한다.
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                containerArr[i][j] = storage[i].charAt(j);
            }
        }
        
        // 처음에는 컨테이너가 모두 존재
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                isExistContainer[i][j] = true;
            }
        }
        int answer = 0;
        
        // request 순회
        for (int k=0; k<requests.length; k++){
            // 바깥과 연결된 컨테이너들의 집합
            Set<int[]> set = new HashSet();
            // request마다 모든 좌표 순회
            for (int i=0; i<n; i++){
                for (int j=0; j<m; j++){
                    // 해당 좌표 값이 request 원하는 값이라면
                    if (containerArr[i][j] == requests[k].charAt(0)){
                        // 만약 길이가 1이라면
                        if (requests[k].length() == 1){
                            if(isConnectedToExternal(i, j)){
                                // 집합에 넣는다.
                                set.add(new int[]{i, j});
                            }
                        }
                        // 만약 길이가 2라면
                        else{
                            set.add(new int[]{i, j});
                        }
                    }
                }
            }
            // 집합에 있는 것들을 모두 뺀다.
            for (int[] temp : set){
                isExistContainer[temp[0]][temp[1]] = false;
            }
        }
        
        // 남아있는 컨테이너 개수 구하기
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (isExistContainer[i][j]){
                    System.out.print(containerArr[i][j]);
                    answer++;
                }
            }
            System.out.println();
        }
        return answer;
    }
    
    /**
        해당 컨테이너가 외부와 연결되어 있는지 판단한다.
        @param x : x 좌표 
        @param y : y 좌표
    */
    private boolean isConnectedToExternal(int startX, int startY){
        int n = containerArr.length;
        int m = containerArr[0].length;
        
        // 방문 여부
        boolean[][] visited = new boolean[n][m];
        
        // BFS로 바깥과 연결되어 있는지 판단한다.
        Queue<int[]> queue = new LinkedList();
        
        // 시작 점을 넣는다.
        queue.add(new int[]{startX, startY});
        visited[startX][startY] = true;
        
        while(!queue.isEmpty()){
            // 꺼낸다.
            int[] current = queue.remove();
            int x = current[0];
            int y = current[1];
            
            for (int i=0; i<4; i++){
                int nx = x+dx[i];
                int ny = y+dy[i];
                // 좌표 넘어가면 외부와 연결되어 있는 것
                if (nx<0 || nx>=n || ny<0 || ny>=m){
                    return true;
                }
                
                // 방문했으면 스킵
                if (visited[nx][ny]){
                    continue;
                }
                
                // 컨테이너가 존재하면 스킵
                if (isExistContainer[nx][ny]){
                    continue;
                }
                
                // 갈 수 있다면 큐에 넣기
                visited[nx][ny] = true;
                queue.add(new int[]{nx, ny});
            }
        }
        return false;
        
    }
}