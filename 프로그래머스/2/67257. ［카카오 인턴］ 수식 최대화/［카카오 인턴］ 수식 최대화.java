import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

class Solution {
    public long solution(String expression) {
        ArrayList<Long> numbers = new ArrayList();
        ArrayList<Character> operators = new ArrayList();
        long currentNumber = expression.charAt(0)-'0';
        for (int i=1; i<expression.length(); i++){
            // 숫자면
            if (Character.isDigit(expression.charAt(i))){
                currentNumber*=10;
                currentNumber+=expression.charAt(i)-'0';
            } 
            // 문자면
            else{
                operators.add(expression.charAt(i));
                numbers.add(currentNumber);
                currentNumber=0;
            }
        }
        // 마지막 값도 더하기
        numbers.add(currentNumber);
        
        // 경우의 수가 많지 않으므로 그냥 6개 경우의 수를 정의한다.
        String[] cases = {"*+-", "*-+", "+*-", "+-*", "-+*", "-*+"};
        long res = 0;
        for (String oneCase: cases){
            ArrayList<Long> newNumbers = new ArrayList(numbers);
            ArrayList<Character> newOperators = new ArrayList(operators);
            res = Math.max(res, Math.abs(getCaseResult(oneCase, newNumbers, newOperators)));
        }
        return res;
    }
    
    // 우선순위에 따라 연산을 한다.
    private long getCaseResult(String sequence, ArrayList<Long> numbers, ArrayList<Character> operators){
        Map<Character, Integer> convertOperatorToIdx = new HashMap();
        convertOperatorToIdx.put(sequence.charAt(0), 0);
        convertOperatorToIdx.put(sequence.charAt(1), 1);
        convertOperatorToIdx.put(sequence.charAt(2), 2);
        // case에 따라 해당 순서대로 연산자가 몇 번 등장했는지 구한다.
        int[] counts = new int[3];
        for (char operator: operators){
            counts[convertOperatorToIdx.get(operator)]++;
        }
        for (int i=0; i<3; i++){
            System.out.println(counts[i]);
        }
        
        // 연산자 우선순위 순서대로 연산 수행한다.
        for (int i=0; i<3; i++){
            char operator = sequence.charAt(i);
            // 해당 우선순위 연산자 등장 횟수만큼 연산 수행
            int cnt = counts[convertOperatorToIdx.get(operator)];
            for (int j=0; j<cnt; j++){
                operate(numbers, operators, operator);
            }
        }
        return numbers.get(0);
        
    }
    
    private void operate(ArrayList<Long> numbers, ArrayList<Character> operators, char operator){
        // 해당 연산자가 처음 나오는 위치를 구한다.
        int operationIdx = -1;
        for (int i=0; i<operators.size(); i++){
            if (operators.get(i) == operator){
                operationIdx = i;
                break;
            }
        }
        
        // 해당 위치를 기준으로 연산한다.
        long firstNumber = numbers.get(operationIdx);
        long secondNumber = numbers.get(operationIdx+1);
        long result = 0;
        if (operator == '*'){
            result = firstNumber*secondNumber;
        }
        if (operator == '-'){
            result = firstNumber-secondNumber;
        }
        if (operator == '+'){
            result = firstNumber+secondNumber;
        }
        
        // 연산한 숫자와 연산자 제거
        numbers.remove(operationIdx);
        numbers.remove(operationIdx);
        operators.remove(operationIdx);
        
        // 새로 연산한 숫자 추가
       	numbers.add(operationIdx, result);
        
    }
}