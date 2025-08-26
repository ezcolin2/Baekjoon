import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine());
        
        ArrayList<Line> lines = new ArrayList<>();
        StringTokenizer st;
        
        while(true) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            if(l == 0 && r == 0) break;
            lines.add(new Line(l, r));
        }
        
        // 시작점 기준 오름차순 정렬
        lines.sort((a, b) -> a.l - b.l);
        
        int currentPos = 0;  // 현재 덮어야 하는 위치
        int idx = 0;
        int count = 0;
        
        while(currentPos < m) {
            int maxRight = currentPos;
            
            // 현재 위치를 덮을 수 있는 선분들 중 가장 오른쪽 끝이 먼 것 찾기
            while(idx < lines.size() && lines.get(idx).l <= currentPos) {
                maxRight = Math.max(maxRight, lines.get(idx).r);
                idx++;
            }
            
            // 더 이상 진행할 수 없으면 실패
            if(maxRight == currentPos) {
                System.out.println(0);
                return;
            }
            
            currentPos = maxRight;
            count++;
        }
        
        System.out.println(count);
    }
    
    static class Line {
        int l, r;
        Line(int l, int r) {
            this.l = l;
            this.r = r;
        }
    }
}