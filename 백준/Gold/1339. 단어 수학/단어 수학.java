/**
    1. 모든 단어를 Set에 넣고 배열로 바꾼다.
    2. 순열을 구하고 계산을 한다.
*/
import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Set;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.HashMap;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String[] arr = new String[n];
        for (int i=0; i<n; i++){
            arr[i] = br.readLine();
        }
        // 등장한 모든 알파벳을 중복 없이 구한다.
        Set<Character> alphabetSet = getAllAlphabet(arr);
        
        // 배열로 바꾼다.
        char[] alphabetArr = new char[alphabetSet.size()];
        int idx = 0;
        for (char alphabet: alphabetSet){
            alphabetArr[idx++] = alphabet;
        }
        Combination combination = new Combination(alphabetArr, arr);
        combination.choose(0);
        bw.write(String.valueOf(combination.maxValue));
        bw.close();
        
    }
    
    /**
        단어들의 배열에서 등장한 모든 알파벳을 중복 없이 집합에 넣어 반환
    */
    public static Set<Character> getAllAlphabet(String[] arr){
        Set<Character> set = new HashSet();
        // 모든 단어 조사
        for (String word: arr){
            // 단어의 모든 알파벳 조사
            for (int i=0; i<word.length(); i++){
                set.add(word.charAt(i));
            }
        }
        return set;
    }
}
class Combination{
    private char[] alphabetArr;
    private String[] wordArr;
    private LinkedList<Character> combination = new LinkedList();
    private boolean[] visited;
    public int maxValue;
    Combination(char[] alphabetArr, String[] wordArr){
        this.alphabetArr = alphabetArr;
        this.visited = new boolean[alphabetArr.length];
        this.wordArr = wordArr;
    }
    /**
        @param idx: 현재까지 고려한 인덱스
        순열을 구하는 함수
    */
    public void choose(int cnt){
        // 다 뽑았다면 계산 시작
        if (cnt == this.alphabetArr.length){
            maxValue = Math.max(maxValue, this.calculate());
        }
        // 모든 경우 전부 고려
        for (int i=0; i<this.alphabetArr.length; i++){
            // 방문한 것은 스킵
            if (visited[i]){
                continue;
            }
            // 방문하지 않았다면 방문
            combination.add(alphabetArr[i]);
            visited[i] = true;
            choose(cnt+1);
            visited[i] = false;
            combination.removeLast();
        }
       
    }
    // 순열을 바탕으로 계산
    public int calculate(){
        // 지금까지 나온 순서대로 9, 8, 7... 매칭하기
        Map<Character, Integer> map = new HashMap();
        int number = 9;
        for (char alphabet: this.combination){
            map.put(alphabet, number--);
        }
        
        // 모든 단어들을 정수로 만들기 
        int[] numberArr = new int[wordArr.length];
        // 모든 단어 순회
        for (int i=0; i<wordArr.length; i++){
            // 단어마다 매칭
            for (int j=0; j<wordArr[i].length(); j++){
                numberArr[i] *= 10;
                numberArr[i] += map.get(wordArr[i].charAt(j));
            }
        }
        
        // 합치기
        int sum = 0;
        for (int currentNumber: numberArr){
            sum += currentNumber;
        }
        return sum;
    }
}