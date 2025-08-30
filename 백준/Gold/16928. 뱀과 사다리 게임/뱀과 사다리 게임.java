import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Map;
import java.util.HashMap;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // map 생성
        Map<Integer, Integer> map = new HashMap<>();
        for (int i=0; i<n+m; i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            map.put(from ,to);
        }

        int minCount = getMinCount(map);
        bw.write(String.valueOf(minCount));
        bw.close();
    }
    private static int getMinCount(Map<Integer, Integer> map){
        boolean[] visited = new boolean[101];
        int[] minCnts = new int[101];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        visited[1] = true;
        while(!queue.isEmpty()){
            int current = queue.remove();
            // 6개 경우의 수 고려
            for (int i=1; i<=6; i++){
                int next = current+i;
                // 범위 벗어나면 스킵
                if (next>100){
                    continue;
                }

                // 방문했다면 스킵
                if (visited[next]){
                    continue;
                }
                
                visited[next] = true;
                minCnts[next] = minCnts[current]+1;
                
                // 만약 사다리 또는 뱀이 있다면
                if (map.containsKey(next)){
                    // 이동
                    int newNext = map.get(next);

                    // 방문했다면 스킵
                    if (visited[newNext]){
                        continue;
                    }
                    visited[newNext] = true;
                    minCnts[newNext] = minCnts[next];
                    queue.add(newNext);
                } else{
                    queue.add(next);
                }

            }
        }
        return minCnts[100];
    }
}

