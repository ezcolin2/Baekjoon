import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.Set;
import java.util.HashSet;

public class Main{


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for (int i=0; i<n; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        // dp[i] : i번째까지 고려했을 때 가장 긴 부분 증가 수열의 길이
        int[] dp = new int[n];
        for (int i=0; i<n; i++){
            dp[i] = 1;
        }
        for (int i=0; i<n; i++){
            // 이전 모든 dp 값들 중 arr[i]보다 작은 값을 가진 dp[i] 중 가장 큰 값으로 갱신
            for (int j=0; j<i; j++){
                if (arr[j] > arr[i]){
                    continue;
                }
                dp[i] = Math.max(dp[i], dp[j]+1);
            }
        }

        bw.write(String.valueOf(n-Arrays.stream(dp).max().getAsInt()));
        bw.close();

    }


}