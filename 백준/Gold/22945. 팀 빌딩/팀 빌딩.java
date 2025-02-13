import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

/**
 * 능력치를 최대로 만들기 위해 고려해야 하는 변수는 두 가지가 있다.
 * 1. 두 개발자 사이 다른 개발자 수
 * 2. 두 개발자의 개인 능력치
 *
 * 두 개발자의 거리를 벌리면서 두 개발자의 개인 능력치가 크면 된다.
 * 무조건 개발자의 거리가 멀다고 능력치가 최대가 되는 것은 아니다.
 * 개발자의 거리가 가깝더라도 두 개발자 모두 개인 능력치가 크다면 팀 능력치가 커질 수 있다.
 * two pointer로 가장 끝 점에서 시작한다.
 * 그리고 두 개발자 중 능력치가 작은 개발자를 이동하면 된다.
 */
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        bw.write(String.valueOf(getMaxTeamScore(arr)));
        bw.close();
    }
    public static int getMaxTeamScore(int[] arr){
        int n = arr.length;
        int maxTeamScore = 0;
        // two pointer
        int left = 0;
        int right = n-1;

        while(left<=right){
            int teamScore = (right-left-1)*Math.min(arr[left], arr[right]);
            maxTeamScore = Math.max(maxTeamScore, teamScore);

            // 능력치가 작은 개발자의 범위를 좁힌다.
            if (arr[left] < arr[right]){
                left++;
            }
            else{
                right--;
            }
        }
        return maxTeamScore;
    }

}