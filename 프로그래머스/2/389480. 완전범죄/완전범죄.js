function solution(info, n, m) {
    const MAX_VALUE = 10000;
    const objectCnt = info.length;
    // dp[i][j][k]: i번 물건까지 고려했을 때 A가 남긴 흔적이 j이고 B가 남긴 흔적이 k인 경우의 가능 여부
    const dp = Array(objectCnt).fill().map(
        ()=>Array(n).fill().map(
            ()=>Array(m).fill(false)
        )
    );
    if (info[0][0] < n){
        dp[0][info[0][0]][0] = true;
    }
    if (info[0][1] < m){
        dp[0][0][info[0][1]] = true;
    }
    
    for (let i=0; i<objectCnt-1; i++){
        for (let j=0; j<n; j++){
            for (let k=0; k<m; k++){
                // 만약 현재 상태가 불가능하다면 스킵
                if (!dp[i][j][k]){
                    continue;
                }
                
                // 다음 물건을 A가 훔쳤을 때
                const nextCntForA = j+info[i+1][0];
                if (nextCntForA < n){
                    dp[i+1][nextCntForA][k] = true;
                }
                // 다음 물건을 B가 훔쳤을 때
                const nextCntForB = k+info[i+1][1];
                if (nextCntForB < m){
                    dp[i+1][j][nextCntForB] = true;
                }                
            }
        }
    }
    let answer = MAX_VALUE;
    for (let j=0; j<n; j++){
        for (let k=0; k<m; k++){
            if (dp[objectCnt-1][j][k]){
                answer = Math.min(answer, j);
            }
        }
    }
    return answer === MAX_VALUE ? -1 : answer;
}