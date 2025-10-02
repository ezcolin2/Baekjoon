import java.util.*;

class Solution {
    private Stack<Integer> combination = new Stack();
    public int[] solution(int[][] dice) {
        int[] res =getMaxCombination(dice);
        for (int i=0; i<res.length; i++){
            System.out.println(res[i]);
        }
        return res;
        
    }
    
    
    // 승리할 확률이 가장 높은 주사위 조합 구하기
    private int[] getMaxCombination(int[][] dices){
        // a의 모든 조합 구하기
        List<List<Integer>> combinations = getDiceCombinations(dices.length);
        
        int maxWinCount = 0;
        int[] res = new int[dices.length/2];
        // a의 모든 조합 
        for (int i=0; i<combinations.size()/2; i++){
            List<Integer> aCombination = combinations.get(i);
            List<Integer> bCombination = combinations.get(combinations.size()-i-1);
            
            List<Integer> aSumCombination = getSumCombination(aCombination, dices);
            List<Integer> bSumCombination = getSumCombination(bCombination, dices);
            Collections.sort(bSumCombination);
            
            // 이제 A가 이기는 횟수를 계산한다.
            int winCount = 0;
            int loseCount = 0;
            
            for (int target: aSumCombination){
                winCount += getLessSumCount(bSumCombination, target);
                loseCount += getMoreSumCount(bSumCombination, target);
            }
            
            // win count가 높다면
            if (maxWinCount < winCount){
                maxWinCount = winCount;
                for (int j=0; j<res.length; j++){
                    res[j] = aCombination.get(j);
                }
            }
            // lose count가 높다면
            if (maxWinCount < loseCount){
                maxWinCount = loseCount;
                for (int j=0; j<res.length; j++){
                    res[j] = bCombination.get(j);
                }
            }
            System.out.println(maxWinCount);
        }
        return res;
    }
    
    private List<List<Integer>> getDiceCombinations(int totalDiceNumber){
        List<Integer> combination = new ArrayList();
        List<List<Integer>> combinations = new ArrayList();
        makeDiceCombinations(combination, combinations, 1, totalDiceNumber);
        return combinations;
    }
    // 주사위 선택 조합 구하기
    private void makeDiceCombinations(List<Integer> combination, List<List<Integer>> combinations, int currentDiceNumber, int n){
        // 끝까지 조사했을 때
        if (currentDiceNumber == n+1){
            // combination이 완성되었다면
            if (combination.size() == n/2){
				combinations.add(new ArrayList(combination));
            }
            return;
        }
        
        // 현재 주사위를 고른다.
        combination.add(currentDiceNumber);
        makeDiceCombinations(combination, combinations, currentDiceNumber+1, n);
        combination.remove(combination.size()-1);
        
        // 고르지 않는다.
        makeDiceCombinations(combination, combinations, currentDiceNumber+1, n);
    }
    
    private List<Integer> getSumCombination(List<Integer> diceCombination, int[][] dices){
        List<Integer> sumCombination = new ArrayList();
        makeSumCombination(sumCombination, diceCombination, dices, 0, 0);
        return sumCombination;
        
    }
    private void makeSumCombination(List<Integer> sumCombination, List<Integer> diceCombination, int[][] dices, int currentDiceIndex, int sum){
        // 다 조사했으면 sum을 추가
        if (currentDiceIndex == diceCombination.size()){
            sumCombination.add(sum);
            return;
        }
        
        // 번호 구하기
        int currentDiceNumber = diceCombination.get(currentDiceIndex);
        
        // 해당 주사위의 모든 경우를 고려
        for (int i=0; i<6; i++){
            // 더하기
            makeSumCombination(sumCombination, diceCombination, dices, currentDiceIndex+1, sum+dices[currentDiceNumber-1][i]);
        }
    }
    
    // 특정 숫자보다 적은 숫자의 개수를 구한다.
    private int getLessSumCount(List<Integer> sumCombination, int target){
        int left = 0;
        int right = sumCombination.size();
        int mid = (left+right)/2;
        while (left<right){
            mid = (left+right)/2;
            if (sumCombination.get(mid) < target){
                left = mid+1;
            } else{
                right = mid;
            }
        }
        return left;
    }
    // 특정 숫자보다 적은 숫자의 개수를 구한다.
    private int getMoreSumCount(List<Integer> sumCombination, int target){
        int left = 0;
        int right = sumCombination.size();
        int mid = (left+right)/2;
        while (left<right){
            mid = (left+right)/2;
            if (sumCombination.get(mid) <= target){
                left = mid+1;
            } else{
                right = mid;
            }
        }
        return sumCombination.size()-left;
    }
    
    private void printAll(List<List<Integer>> combinations){
        for (List<Integer> combination: combinations){
            for (int element: combination){
                System.out.print(element);
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}
