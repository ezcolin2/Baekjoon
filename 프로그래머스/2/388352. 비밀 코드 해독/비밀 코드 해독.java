import java.util.Set;
import java.util.HashSet;
class Solution {
    private Set<Integer> password;
    private int possiblePasswordCount;
    public int solution(int n, int[][] q, int[] ans) {
        password = new HashSet();
        possiblePasswordCount = 0;
        getPossiblePasswordCount(n, 1, 0, q, ans);
        
        return possiblePasswordCount;
    }
    
    /**
        @param password : 5개의 서로 다른 숫자의 집합
        @param q : m개의 질문들
        @param ans : 각 질문마다 맞춘 개수
    */
    private boolean isPossiblePassword(Set<Integer> password, int[][] q, int[] ans){
        // 각 질문 별 맞춘 개수
        int[] countArr = new int[q.length];
        
        // 각 질문 순회
        for (int i=0; i<q.length; i++){
            // 질문에서 입력한 정수들이 set에 존재하는지 확인
            for (int j=0; j<5; j++){
                // 없으면 스킵
                if (!password.contains(q[i][j])){
                    continue;
                }
                // 있으면 증가
                countArr[i]++;
            }
        }
        
        // ans와 동일한지 확인
        for (int i=0; i<ans.length; i++){
            // 다르면 false 반환
            if (countArr[i] != ans[i]){
                return false;
            }
        }
        return true;
    }
    
    /**
        @param number : 현재 고르려는 숫자
        @param count : 지금까지 고른 숫자 개수
    */
    private void getPossiblePasswordCount(int n, int number, int count, int[][] q, int[] ans){
        // 다 골랐다면 해당 비밀번호가 가능한지 확인
        if (number > n+1){
            return;
        }
        if (count == 5){
            if (isPossiblePassword(password, q, ans)){
                
                possiblePasswordCount++;
            }
            return;
        }
        
        // number를 고른다면
        password.add(number);
        getPossiblePasswordCount(n, number+1, count+1, q, ans);
        password.remove(number);
        
        // number를 고르지 않는다면
        getPossiblePasswordCount(n, number+1, count, q, ans);
        
         
    }
}