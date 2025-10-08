import java.util.*;
import java.util.stream.*;

/**
    1. 모든 과녁 점수에 대해 (승/패/무) 경우의 수를 구한다. (3^11 = 177147)
    2. 각 경우의 수가 n개의 화살을 써서 가능한 경우인지 확인한다.
    3. 가능하다면 가장 높은 점수를 얻을 수 있는 경우의 수만 남긴다.
    4. 남은 경우의 수를 기반으로 각 점수마다 맞춰야 하는 화살의 최소 개수를 구한다.
    5. 화살이 남을 수 있는데 이건 1개 이상 맞춘 과녁의 점수 중 가장 작은 점수에 남는 화살을 다 넣는다.
    6. 계속 갱신한다.
*/

class Solution {
    public int[] solution(int n, int[] info) {
        // 가능한 경우의 수를 모두 구한다.
        List<String> combinations = getCombinations(info, n);
        return getHighPriorityCombination(info, n, combinations);
        
    }
    
    // 가장 우선순위가 높은 것 구하기
    private int[] getHighPriorityCombination(int[] info, int n, List<String> combinations){
        String combination = combinations.get(0);
        
        // 높은 순 정렬
        Collections.sort(combinations, (a, b)->getScoreDistance(info, b)-getScoreDistance(info, a));
        
        // 근데 가장 높은 게 0이하라면
        if (getScoreDistance(info, combinations.get(0)) <=0){
            return new int[]{-1};
        }
        
        int[][] filteredCombinations = combinations.stream().filter(a -> getScoreDistance(info, a) == getScoreDistance(info, combinations.get(0))).map(a -> getCombinationArrowCount(info, n, a)).toArray(int[][] :: new);
        
        Arrays.sort(filteredCombinations, (a, b) -> {
            for (int i=a.length-1; i>=0; i--){
                // 다를 때
                if (a[i] != b[i]){
                    return b[i]-a[i];
                }
            }
            return 0;
        });
        return filteredCombinations[0];
    }
    
    private int getScoreDistance(int[] info, String combination){
        int lion = 0;
        int apeach = 0;
        for (int i=0; i<11; i++){
            // 승리라면
            if (combination.charAt(i) == '0'){
                lion += 10-i;
            }
            
            // 패배라면
            else if (combination.charAt(i) == '1'){
                apeach += 10-i;
            }
        }
        
        return lion-apeach;
    }
    
    private int[] getCombinationArrowCount(int[] info, int n, String combination){
        int[] combinationArrowCount = new int[info.length];
        int totalArrowCount = 0;
        
        // 모든 경우 순회
        for (int i=0; i<info.length; i++){
            
            // 만약 라이언이 이기는 경우라면
            if (combination.charAt(i) == '0'){
                // 어피치가 맞힌 화살 개수 +1 만큼 맞추기
                totalArrowCount += info[i]+1;
                combinationArrowCount[i] = info[i]+1;
            }
        }
        
        // 남았다면 마지막 부분에 남은 거 0점에 쏘기
        if (totalArrowCount < n){
            combinationArrowCount[10] += n-totalArrowCount;
        }
        return combinationArrowCount;
    }
    
    private List<String> getCombinations(int[] info, int n){
        List<String> combinations = new ArrayList();
        StringBuffer combination = new StringBuffer();
        makeCombinations(info, n, combinations, combination);
        
        return combinations;
    }
    
    private void makeCombinations(int[] info, int n, List<String> combinations, StringBuffer combination){
        // 다 구했다면
        if (combination.length() == 11){
            if (isPossibleCombination(info, n, combination.toString())){
                combinations.add(combination.toString());
            }
            return;
        }
        
        // 아직 다 구하지 않았다면 3가지 경우의 수 고려
        for (int i=0; i<3; i++){
            // 삽입
            combination.append((char) (i+'0'));
            makeCombinations(info, n, combinations, combination);
            // 빼기
            combination.deleteCharAt(combination.length()-1);
        }
    }
    
    // 화살 n개를 써서 만들 수 있는 경우의 수인지
    private boolean isPossibleCombination(int[] info, int n, String combination){
        int totalArrowCount = 0;
        
        // 모든 경우 순회
        for (int i=0; i<info.length; i++){
            // 무승부는 둘 다 맞추지 못 했을 때만 가능한데 어피치가 맞춘 점수라면 불가능
            if (combination.charAt(i) == '2'){
                if (info[i]>0){
                    return false;
                }
            }
            
            // 만약 라이언이 이기는 경우라면
            if (combination.charAt(i) == '0'){
                // 어피치가 맞힌 화살 개수 +1 만큼 맞추기
                totalArrowCount += info[i]+1;
            }
            
            // 라이언이 지는 경우인데 어피치가 맞힌 화살 개수가 0이라면 불가능
            if (combination.charAt(i) == '1'){
                if (info[i] == 0){
                    return false;
                }
                
            }
        }
        // 불가능한 경우는 제외하고 이제 화살의 개수가 n개 이하로 써서 가능한지 확인한다.
        return totalArrowCount <= n;
    }
}