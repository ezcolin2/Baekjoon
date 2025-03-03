import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.lang.Math;

public class Main{
    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken()); // 목표 cpu
        int k = Integer.parseInt(st.nextToken()); // 목표 메모리

        int[][] tabArr = new int[n+1][3];
        for (int i=1; i<=n; i++){
            st = new StringTokenizer(br.readLine());
            tabArr[i][0] = Integer.parseInt(st.nextToken());
            tabArr[i][1] = Integer.parseInt(st.nextToken());
            tabArr[i][2] = Integer.parseInt(st.nextToken());
        }

        // dp[i][j][k] : i번째 탭까지 고려했을 때 cpu가 j, 중요도가 k일 때 최대 메모리
        // cpu가 m이 넘을 경우 m으로 처리하기 위해 최대 m까지
        // 중요도는 최대 5이고 크롬 탭이 100개이기 때문에 최대 500
        int[][][] dp = new int[n+1][m+1][501];

        // 모든 값을 -INF로 초기화 한다.
        for (int i=0; i<=n; i++){
            for (int j=0; j<=m; j++){
                for (int p=0; p<=500; p++){
                    dp[i][j][p] = Integer.MIN_VALUE;
                }
            }
        }

        // 아무것도 없을 때
        dp[0][0][0] = 0;

        for (int i=1; i<=n; i++){
            int cpu = tabArr[i][0];
            int memory = tabArr[i][1];
            int importance = tabArr[i][2];
            for (int j=0; j<=m; j++){
                for (int p=0; p<=500; p++){
                    // tabArr[i]를 선택하지 않는 경우
                    dp[i][j][p] = Math.max(dp[i][j][p], dp[i-1][j][p]);
                    // tabArr[i]를 선택하는 경우
                    // 만약 cpu가 m이 넘을 경우 m으로 처리한다.
                    int nextCpu = Math.min(m, j+cpu);

                    // importance는 500을 넘을 수 없다.
                    int nextImportance = p+importance;
                    if (nextImportance > 500){
                        continue;
                    }

                    dp[i][nextCpu][nextImportance] = Math.max(
                            dp[i][nextCpu][nextImportance],
                            dp[i-1][j][p]+memory
                    );

                }
            }
        }

        int res = Integer.MAX_VALUE;
        for (int i=0; i<=500; i++){
            if (dp[n][m][i] >= k){
                res = i;
                break;
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        if (res == Integer.MAX_VALUE){
            bw.write("-1");
        }
        else{
            bw.write(String.valueOf(res));
        }
        bw.close();


    }
}