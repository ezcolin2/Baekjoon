import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;
import java.lang.Math;

/**
 * 변수
 * 1. 데드라인
 * 2. 컵라면 수
 * 데드라인을 늘리면서 해당 데드라인에서 얻을 수 있는 최대 컵라면 수를 고른다면?
 * 현재 시점에서 최적의 선택이 최적의 해가 아닐 수 있다.
 * 현재의 선택이 다음 선택에 영향을 주게 된다.
 * 예를 들어 데드라인이 1이고 컵라면 수가 1인 것과 데드라인이 2이고 컵라면 수가 9인 것이 있다고 하자.
 * 데드라인이 1일 때 최적의 선택은 데드라인이 2인 문제를 푸는 것이다.
 * 그런데 데드라인이 2인 문제를 풀어버리면 다음 데드라인 2일 때 아무것도 선택하지 못 한다.
 * 데드라인이 1일 때 1인 문제를 풀고 2일 때 2인 문제를 풀어야 최적의 해가 된다.
 *
 * 그래서 데드라인을 줄이면서 최대 컵라면 수를 고르면 최적의 선택이 최적의 해가 된다.
 *
 */
public class Main{
    public static int[][] problems;
    public static Queue<Integer> priorityQueue;
    public static int n;
    public static void main(String[] args) throws IOException{
        priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        problems = new int[n+1][2];
        StringTokenizer st;
        for (int i=1; i<=n; i++){
            st = new StringTokenizer(br.readLine());
            problems[i][0] = Integer.parseInt(st.nextToken());
            problems[i][1] = Integer.parseInt(st.nextToken());
        }

        int maxCup = getMaxCups();
        bw.write(String.valueOf(maxCup));
        bw.close();


    }

    /**
     * 가장 많이 얻을 수 있는 컵라면 수를 반환한다.
     * @return 최대 컵라면 수
     */
    public static int getMaxCups(){
        int maxCup = 0;
        // 각 deadline 별 컵라면 개수를 구한다.
        List<Integer>[] cupArr = getCupList();

        // 우선순위 큐
        Queue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        // 거꾸로 조사한다.

        for (int i=n; i>0; i--){
            // 모두 넣는다.
            for (Integer integer:cupArr[i]){
                priorityQueue.add(integer);
            }

            // 가장 컵라면 수가 많은 것을 뽑는다.
            if (!priorityQueue.isEmpty()){
                maxCup += priorityQueue.poll();

            }
        }
        return maxCup;
    }

    public static List<Integer>[] getCupList(){
        List<Integer>[] arr = new ArrayList[n+1];
        for (int i = 0; i <= n; i++) {
            arr[i] = new ArrayList<>();
        }
        for (int i=1; i<=n; i++){
            int deadline = problems[i][0];
            int cups = problems[i][1];
            arr[deadline].add(cups);

        }
        return arr;
    }
}