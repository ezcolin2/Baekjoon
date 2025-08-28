import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        // 최대 높이 구하기
        int maxHeight = Math.max(a, b);

        // 최대 높이 빌딩의 위치 범위
        int left = a-1;
        int right = n-b;
        if (left>right){
            bw.write(String.valueOf(-1));
            bw.close();
            return;
        }

        // 사전 순이기 때문에 가장 뒤로
        int[] heights = new int[n];
        heights[right] = maxHeight;
        int danbiHeight = b-1;
        for (int i=right+1; i<n; i++){
            // 단비 기준
            if(danbiHeight == 1){
                heights[i] = 1;
                continue;
            }
            heights[i] = danbiHeight--;
        }
        int gahuiHeight = a-1;
        if (gahuiHeight > 0){
            for(int i=right-1; i>=0; i--){
                // 가희 기준
                if(gahuiHeight == 1){
                    heights[i] = 1;
                    continue;
                } else if (gahuiHeight == 0){
                    heights[i] = maxHeight;
                    continue;
                }
                heights[i] = gahuiHeight--;
            }
        } else{
            for(int i=right; i>0; i--){
                heights[i] = 1;
            }
            heights[0] = maxHeight;

        }
        for(int i=0; i<n; i++){
            bw.write(String.valueOf(heights[i]));
            bw.write(' ');
        }
        bw.close();
    }
}

