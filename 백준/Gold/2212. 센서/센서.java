import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main{
    public static int[] getIntervalOfSensors(int[] sensors){
        // sensor 사이 간격을 구한다.
        int[] intervals = new int[sensors.length-1];

        for (int i=0; i<sensors.length-1; i++){
            intervals[i] = sensors[i+1] - sensors[i];
        }

        // 오름차순 정렬
        Arrays.sort(intervals);
        return intervals;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] sensors = new int[n];
        for (int i=0; i<n; i++){
            sensors[i] = Integer.parseInt(st.nextToken());
        }

        // sensor 오름차순 정렬
        Arrays.sort(sensors);

        // 기지국 한 개일 때 거리 구하기
        int sumOfInterval = sensors[sensors.length-1] - sensors[0];

        // 간격 구하기
        int[] intervals = getIntervalOfSensors(sensors);

        // k개까지 기지국 설치
        // 가장 큰 간격부터 없앰
        for (int i=intervals.length-1; i>Math.max(intervals.length-k, -1); i--){
            sumOfInterval -= intervals[i];
        }

        System.out.println(sumOfInterval);

    }
}