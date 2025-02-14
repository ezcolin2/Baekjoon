import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] times = new int[n + 2];
        int[] prices = new int[n + 2];
        int[] dp = new int[n + 2];

        StringTokenizer st;
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            times[i] = Integer.parseInt(st.nextToken());
            prices[i] = Integer.parseInt(st.nextToken());
        }

        // DP 역순 탐색
        for (int i = n; i > 0; i--) {
            // 일단 다음 날의 최대 이익을 현재에 반영
            dp[i] = dp[i + 1];

            int end = i + times[i];
            if (end <= n + 1) {
                dp[i] = Math.max(dp[i], dp[end] + prices[i]);
            }
        }

        bw.write(String.valueOf(dp[1]));
        bw.close();
    }
}
