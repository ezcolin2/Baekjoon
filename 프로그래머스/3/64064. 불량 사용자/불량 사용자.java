import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Collections;
import java.util.Arrays;

class Solution {
    private ArrayList<String> combination = new ArrayList();
    private String[] userIds;
    private String[] bannedIds;
    private boolean[] isChosened;
    private Set<String> set = new HashSet();
    public int solution(String[] userIds, String[] bannedIds) {
        this.userIds = userIds;
        this.bannedIds = bannedIds;
        this.isChosened = new boolean[userIds.length];
        makeCombination(0);
        return set.size();
    }
    
    private void makeCombination(int currentIndex){
        // 끝까지 탐색
        if (currentIndex == bannedIds.length){
            // 만약 banned_id 개수만큼 뽑았다면
            if (combination.size() == bannedIds.length){
                ArrayList<String> newCombination = new ArrayList(combination);
                Collections.sort(newCombination);
                String setKey = String.join(":", newCombination);
                set.add(setKey);
            }
            return;
        }
        // bannedIds[currentIndex]에 해당하는 것을 찾기
        for (int i=0; i<userIds.length; i++){
            // 이미 뽑았다면 스킵
            if (isChosened[i]){
                continue;
            }
            
            // 만약 뽑을 수 없다면 스킵
            if (!canBanned(userIds[i], bannedIds[currentIndex])){
                continue;
            }
            
            combination.add(String.valueOf(i));
            isChosened[i] = true;
            makeCombination(currentIndex+1);
            isChosened[i] = false;
            combination.remove(combination.size()-1);
            
        }

        
    }
    
    private boolean canBanned(String userId, String banId){
        if (userId.length() != banId.length()){
            return false;
        }
        for (int i=0; i<userId.length(); i++){
            if (banId.charAt(i) == '*'){
                continue;
            }
            if (userId.charAt(i) != banId.charAt(i)){
                return false;
            }
        }
        return true;
    }
}