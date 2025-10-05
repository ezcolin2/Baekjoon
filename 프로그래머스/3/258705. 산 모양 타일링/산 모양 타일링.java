class Solution {
    public int solution(int n, int[] tops) {
        int[] dp = new int[2*n+1];
        dp[0] = 1;
        
        // 층 여부에 따라 달라짐
        if (tops[0] == 1){
            dp[1] = 3;
        } else{
            dp[1] = 2;
        }
        
        // 시작
        for (int i=2; i<2*n+1; i++){
            // 홀수번째라면 (0부터 시작했으니 짝수로 판단)
            if (i%2 == 0){
                dp[i] = (dp[i-1]+dp[i-2])%10007;
            }
            // 짝수번째라면 
            else{
                // 2층이라면 
                if (tops[i/2] == 1){
                    dp[i] = (dp[i-1]*2 + dp[i-2])%10007;
                } else{
                    dp[i] = (dp[i-1] + dp[i-2])%10007;
                }
            }
        }
        
        return dp[n*2];
    }
}