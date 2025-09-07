import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public int[] solution(String s) {
        // 튜플 리스트를 길이 순서대로 정렬
        ArrayList<Integer>[] tupleList = getTupleList(s);
        Arrays.sort(tupleList, (a, b)->a.size()-b.size());
		int[] answer = new int[tupleList.length];
        Set<Integer> set = new HashSet();
        for (int i=0; i<tupleList.length; i++){
            for (int j=0; j<tupleList[i].size(); j++){
                int number = tupleList[i].get(j);
                if (!set.contains(number)){
                    set.add(number);
                    answer[i] = number;
                }
            }
        }
        
        return answer;
    }
    
    private ArrayList<Integer>[] getTupleList(String s){
        // 튜플 개수의 길이를 가지는 배열 생성
        int tupleCnt = getTupleCnt(s);
        ArrayList<Integer>[] tupleList = new ArrayList[tupleCnt];
        for (int i=0; i<tupleCnt; i++){
            tupleList[i] = new ArrayList();
        }
        
        // 배열 채우기
        int tupleListIndex = 0;
        for (int i=0; i<s.length(); i++){
            char character = s.charAt(i);
            if (character == '{' || character == ','){
                continue;
            }
            if (character == '}'){
                tupleListIndex++;
                continue;
            }
            
            if (Character.isDigit(character)){
                // 만약 두 자리 수 이상이라면 기존 값에 추가
                if (Character.isDigit(s.charAt(i-1))){
                    ArrayList<Integer> tuple = tupleList[tupleListIndex];
                    tuple.set(tuple.size()-1, tuple.get(tuple.size()-1)*10 + character-'0');
                }
                else{
                    tupleList[tupleListIndex].add(character-'0');
                    
                }
            }
        }
        
        return tupleList;
    }
    
    private int getTupleCnt(String s){
        int cnt = 0;
        for (int i=0; i<s.length(); i++){
            if (s.charAt(i) == '{'){
                cnt++;
            }
        }
        return cnt-1;
    }
}