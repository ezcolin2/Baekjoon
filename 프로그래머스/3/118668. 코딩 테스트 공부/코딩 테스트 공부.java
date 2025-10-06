import java.util.*;

class Solution {
    public int solution(int alp, int cop, int[][] problems) {
        return getMinTime(alp, cop, problems);
    }
    
    private int getMinTime(int startAlp, int startCop, int[][] problems){
        int maxAlp = 0;
        int maxCop = 0;
        for (int[] problem: problems){
            maxAlp = Math.max(maxAlp, problem[0]);
            maxCop = Math.max(maxCop, problem[1]);
        }
        // 초기화
        int[][] dp = new int[151][151];
        for (int i=0; i<151; i++){
            for (int j=0; j<151; j++){
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        dp[startAlp][startCop] = 0;
        
        // 큐 생성
        Queue<int[]> queue = new PriorityQueue<int[]>((a, b)->a[2]-b[2]);
        queue.add(new int[]{startAlp, startCop, 0});
        
        // 시작
        while (!queue.isEmpty()){
            int[] current = queue.remove();
            int alp = current[0];
            int cop = current[1];
            if (current[2] != dp[alp][cop]){
                continue;
            }
            // 알고리즘 공부
            if (alp+1 <= 150){
                if (dp[alp+1][cop] > dp[alp][cop]+1){
                    dp[alp+1][cop] = dp[alp][cop]+1;
                    queue.add(new int[]{alp+1, cop, dp[alp+1][cop]});
                }
            }

            // 코딩 공부
            if (cop+1 <= 150){
                if (dp[alp][cop+1] > dp[alp][cop]+1){
                    dp[alp][cop+1] = dp[alp][cop]+1;
                    queue.add(new int[]{alp, cop+1, dp[alp][cop+1]});
                }
            }

            // 모든 문제들을 보면서 풀 수 있다면 풀기
            for (int[] problem: problems){
                int alp_req = problem[0];
                int cop_req = problem[1];
                int alp_rwd = problem[2];
                int cop_rwd = problem[3];
                int cost = problem[4];
                if (alp_req <= alp && cop_req <= cop){
                    int newAlp = Math.min(150, alp+alp_rwd);
                    int newCop = Math.min(150, cop+cop_rwd);
                    if (dp[newAlp][newCop] > dp[alp][cop]+cost){
                        dp[newAlp][newCop] = dp[alp][cop]+cost;
                        queue.add(new int[]{newAlp, newCop, dp[newAlp][newCop]});
                    }
                }
            }
        }
        // 이제 maxAlp와 maxDlp이상의 것들을 모두 조사한다.
        int res = Integer.MAX_VALUE;
        for (int alp = maxAlp; alp<=150; alp++){
            for (int cop = maxCop; cop<=150; cop++){
                res = Math.min(res, dp[alp][cop]);
            }
        }
        return res;
    }
}