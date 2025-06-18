import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Solution{
	public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for (int i=0; i<t; i++){
        	st = new StringTokenizer(br.readLine());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            bw.write(String.valueOf(getMaxScore(b, w, x, y, z)));
            bw.write('\n');
        }
        bw.close();
    }
    public static int getMaxScore(int b, int w, int x, int y, int z){
    	// 우선 b, w중 작은 값을 기준 값으로 정한다.
        // 작은 값을 선택하는 이유 : 같은 색상 상자에 몇 개를 넣을 지 결정하기 쉽다.
        int standard = Math.min(b, w);
        int maxScore = Integer.MIN_VALUE;
        // 같은 색상 상자에 넣는 개수의 모든 경우를 계산해본다.
        for (int cnt=0; cnt<=standard; cnt++){
        	// 검은 색이 기준이라면
            if (standard == b){
                // 검은 상자에 들어있는 검은 공의 개수
                int sameBlackCnt = cnt;
                
                // 검은 상자에 들어있는 하얀 공의 개수
                int differentBlackCnt = b-cnt;
                
                // 하얀 상자에 들어있는 하얀 공의 개수
                int sameWhiteCnt = w-b+cnt;
                
                // 하얀 상자에 들어있는 검은 공의 개수
                int differentWhiteCnt = b-cnt;
                
                // 계산
                maxScore = Math.max(maxScore, sameBlackCnt*x + sameWhiteCnt*y + (differentBlackCnt+differentWhiteCnt)*z);
            }
            // 하얀 색이 기준이라면
            else{
                // 하얀 상자에 들어있는 하얀 공의 개수
                int sameWhiteCnt = cnt;
                
                // 하얀 상자에 들어있는 검은 공의 개수
                int differentWhiteCnt = w-cnt;
                
                // 검은 상자에 들어있는 검은 공의 개수
                int sameBlackCnt = b-w+cnt;
                
                // 검은 상자에 들어있는 하얀 공의 개수
                int differentBlackCnt = w-cnt;
                
                // 계산
                maxScore = Math.max(maxScore, sameBlackCnt*x + sameWhiteCnt*y + (differentBlackCnt+differentWhiteCnt)*z);
            }
        }
        return maxScore;
    }  
}