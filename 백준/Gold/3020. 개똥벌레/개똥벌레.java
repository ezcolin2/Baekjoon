import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int[] fromDownHeights = new int[n/2]; // 석순 
        int[] fromTopHeights = new int[n/2]; // 종유석 
        for (int i=0; i<n; i++){
            if (i%2==0){
                fromDownHeights[i/2] = Integer.parseInt(br.readLine());
            } else{
                fromTopHeights[i/2] = Integer.parseInt(br.readLine());
            }
        }

        // 오름차순 정렬
        Arrays.sort(fromDownHeights);
        Arrays.sort(fromTopHeights);

        int res = Integer.MAX_VALUE;
        int[] heightCntArr = new int[n+1];

        // 각 높이 별로 모두 구하기
        for (int height=1; height<=h; height++){
            // 석순부터 해당 높이를 마지막에 끼워넣을 위치
            int bottomCnt = n/2-bisectLeft(fromDownHeights, height);

            // 종유석
            int newHeight = h-height+1;
            int topCnt = n/2-bisectLeft(fromTopHeights, newHeight);
            heightCntArr[bottomCnt+topCnt]++;
            res = Math.min(res, bottomCnt+topCnt);
        }

        bw.write(String.valueOf(res));
        bw.write(" ");
        bw.write(String.valueOf(heightCntArr[res]));
        bw.close();
    }

    private static int bisectLeft(int[] arr, int value){
        int left=0;
        int right = arr.length;
        while(left<right){
            int mid = (left+right)/2;
            if (arr[mid]<value){
                left=mid+1;
            } else {
                right=mid;
            }
        }
        return left;
    }
    private static int bisectRight(int[] arr, int value){
        int left=0;
        int right=arr.length;
        while (left<right){
            int mid = (left+right)/2;
            if (arr[mid]<=value){
                left=mid+1;
            } else{
                right=mid;
            }
        }
        return left;
    }
}

