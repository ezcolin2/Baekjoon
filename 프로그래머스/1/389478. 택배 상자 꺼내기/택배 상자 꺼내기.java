class Solution {
    // 동서남북
    public int[] dx = {0, 0, 1, -1};
    public int[] dy = {1, -1, 0, 0};
    
    public int solution(int n, int w, int num) {
        int h = (int) Math.ceil(((double)n/w));
        System.out.println(h);
        int[][] warehouse = new int[h][w];
        // 쌓기 시작
        Location currentLocation = new Location(h-1, 0);
        for (int i=1; i<=n; i++){
            // 택배 쌓음
            warehouse[currentLocation.x][currentLocation.y] = i;
            // 이동
            currentLocation = nextLocation(h, w, i, currentLocation);
        }
        // 택배 번호가 위치한 위치 찾기
        Location location = findLocationByNumber(warehouse, num);
        
        // 가장 위가 비어있는지
        boolean isTopEmpty = warehouse[0][location.y] == 0;
        int res = location.x+1;
        
        // 만약 비어있다면 1 빼기
        if (isTopEmpty){
            res--;
        }
        return res;
    }
    // 차례대로 쌓을 때 다음 위치
    public Location nextLocation(int n, int w, int number, Location currentLocation){
        // 홀수 층이면
        if (isOddFloor(n, w, number)){
            // 오른쪽 끝이면
            if (currentLocation.y == w-1){
                // 위로 이동
                return new Location(currentLocation.x-1, currentLocation.y);
            }
            // 오른쪽 끝이 아니면 오른쪽으로 이동
            return new Location(currentLocation.x, currentLocation.y+1);
        }
        // 짝수 층이면
        // 왼쪽 끝이면
        if (currentLocation.y == 0){
            // 위로 이동
            return new Location(currentLocation.x-1, currentLocation.y);
        }
        // 왼쪽 끝이 아니면 왼쪽으로 이동
        return new Location(currentLocation.x, currentLocation.y-1);
    }
    
    public boolean isOddFloor(int n, int w, int number){
        return ((number-1)/w)%2==0;
    }
    
    public Location findLocationByNumber(int[][] warehouse, int number){
        int n = warehouse.length;
        int w = warehouse[0].length;
        for (int i=0; i<n; i++){
            for (int j=0; j<w; j++){
                if (warehouse[i][j] == number){
                    return new Location(i, j);
                }
            }
        }
        return new Location(-1, -1);
    }

}
class Location{
    int x;
    int y;
    Location(int x, int y){
        this.x = x;
        this.y = y;
    }
}