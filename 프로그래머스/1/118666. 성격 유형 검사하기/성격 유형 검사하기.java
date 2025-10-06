import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        Map<Character, Integer> scoreMap = getScoreMap(survey, choices);
        return getCharacterType(scoreMap);
    }
    
    // 총 점수를 구한다.
    private Map<Character, Integer> getScoreMap(String[] survey, int[] choices){
        Map<Character, Integer> scoreMap = new HashMap();
        scoreMap.put('R', 0);
        scoreMap.put('T', 0);
        scoreMap.put('C', 0);
        scoreMap.put('F', 0);
        scoreMap.put('J', 0);
        scoreMap.put('M', 0);
        scoreMap.put('A', 0);
        scoreMap.put('N', 0);
        
        for (int i=0; i<survey.length; i++){
            // 비동의한다면
            if (choices[i] < 4){
                // 첫 번째 캐릭터 점수 획득
                int score = 4-choices[i];
                scoreMap.put(survey[i].charAt(0), scoreMap.get(survey[i].charAt(0))+score);
            } 
            // 동의한다면
            if (choices[i] > 4){
                // 두 번째 캐릭터 점수 획득
                int score = choices[i]-4;
                scoreMap.put(survey[i].charAt(1), scoreMap.get(survey[i].charAt(1))+score);
            }
        }
        
        return scoreMap;
    }
    
    // 점수보고 결정
    private String getCharacterType(Map<Character, Integer> scoreMap){
        String characterType = "";
        // 1번 지표
        if (scoreMap.get('R') >= scoreMap.get('T')){
            characterType+="R";
        } else{
            characterType+="T";
        }
        
        // 2번 지표
        if (scoreMap.get('C') >= scoreMap.get('F')){
            characterType+="C";
        } else{
            characterType+="F";
        }
        
        // 3번 지표
        if (scoreMap.get('J') >= scoreMap.get('M')){
            characterType+="J";
        } else{
            characterType+="M";
        }
        
        // 4번 지표
        if (scoreMap.get('A') >= scoreMap.get('N')){
            characterType+="A";
        } else{
            characterType+="N";
        }
        
        return characterType;
    }
}