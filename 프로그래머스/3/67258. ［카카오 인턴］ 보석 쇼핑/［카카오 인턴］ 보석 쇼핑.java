import java.util.Set;
import java.util.HashSet;
import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] solution(String[] gems) {
        int totalGemCnt = getTotalGemCnt(gems);
        int minStartIdx=Integer.MAX_VALUE;
        int minLength=Integer.MAX_VALUE;
        // parametric search
        int left=1;
        int right=gems.length;
    
        while (left<=right){
            int mid = (left+right)/2;
            int startIdx = getStartIdxOfPossibleLength(gems, mid, totalGemCnt);
            // 만약 가능하면 길이와 시작 인덱스를 함께 갱신
            if (startIdx>-1){
                // 지금까지 갱신된 최소 길이보다 작으면 길이와 startIdx 무조건 갱신
                if (mid<minLength){
                    minLength = mid;
                    minStartIdx = startIdx;
                }
                // 더 작은 값이 가능한지 확인
                right=mid-1;
            }
            
            // 불가능하다면
            else{
                left=mid+1;
            }
        }
        return new int[]{minStartIdx+1, minStartIdx+minLength};
    }
    
    // 조건을 만족하는 length 길이의 구간의 첫 번째 시작 인덱스 구하기 (없으면 -1)
    private int getStartIdxOfPossibleLength(String[] gems, int length, int totalGemCnt){
        int minStartIdx = -1;
        int gemCnt = 0;
        Map<String, Integer> gemCnts = new HashMap();
        // 일단 인덱스 0부터 length 길이의 구간을 map에 넣기
        for (int i=0; i<length; i++){
            // 존재하면 추가
            if (gemCnts.containsKey(gems[i])){
                gemCnts.put(gems[i], gemCnts.get(gems[i])+1);
            }
         	// 없으면 1로 세팅
            else{
                gemCnts.put(gems[i], 1);
                gemCnt++;
            }
        }
        if (gemCnt==totalGemCnt){
            return 0;
        }
		
        // 모든 구간을 확인 
        for (int i=1; i<=gems.length-length; i++){
            // 우선 첫 번째 구간 제거
            if (gemCnts.get(gems[i-1]) == 1){
                gemCnts.remove(gems[i-1]);
                gemCnt--;
            } else{
                gemCnts.put(gems[i-1], gemCnts.get(gems[i-1])-1);
            }
            
            // 마지막 구간 추가
            // 존재하면 추가
            if (gemCnts.containsKey(gems[i+length-1])){
                gemCnts.put(gems[i+length-1], gemCnts.get(gems[i+length-1])+1);
            }
         	// 없으면 1로 세팅
            else{
                gemCnts.put(gems[i+length-1], 1);
                gemCnt++;
            }
            
            // 만약 모든 종류를 구했다면
            if (gemCnt == totalGemCnt){
                minStartIdx = i;
                break;
            }
        }
        return minStartIdx;
    }
    // 모든 보석의 종류 수
    private int getTotalGemCnt(String[] gems){
        Set<String> set = new HashSet();
        for (String gem: gems){
            set.add(gem);
        }
        return set.size();
    }
}