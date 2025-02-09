import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static int[] arr;
    public static int n;
    public static int m;
    public static int k;


    /**
     *
     * @param minDistance 심판 사이 최소 거리
     * @return 심판 사이 최소 거리를 유지하면서 심판을 배치하는 것이 가능한지
     */
    public static boolean isPossible(int minDistance){
        int previousLocation = 0; // 이전 심판 위치
        int cnt = 1;
        for (int i=1; i<k; i++){
            // 최소 거리 만족하지 않으면 스킵
            if (arr[i]-arr[previousLocation] < minDistance){
                continue;
            }

            cnt++;
            previousLocation=i;
        }
        return cnt>=m;
    }

    /**
     * parametric search
     * @return 최소 거리
     */
    public static int getMinDistance(){
        int left=0;
        int right=n;
        int res = 0;
        while (left<=right){
            int mid = (left+right)/2;
            // 가능하다면 더 높이기
            if (isPossible(mid)){
                left = mid+1;
                res = Math.max(res, mid);
            }
            else{
                right = mid-1;
            }
        }
        return res;
    }

    public static String getRes(int minDistance){
        int previousLocation = 0; // 이전 심판 위치
        String res = "1";
        int count = 1;
        for (int i=1; i<k; i++){
            // 최소 거리 만족하지 않거나 모든 심판을 배치했다면 스킵
            if (arr[i]-arr[previousLocation] < minDistance || count >=m){
                res += "0";
                continue;
            }

            previousLocation=i;
            res += "1";
            count++;
        }
        return res;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken()); // 트랙 길이
        m = Integer.parseInt(st.nextToken()); // 심판 수
        k = Integer.parseInt(st.nextToken()); // 정해진 곳

        arr = new int[k];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<k; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int minDistance = getMinDistance();
        System.out.println(getRes(minDistance));
    }
}