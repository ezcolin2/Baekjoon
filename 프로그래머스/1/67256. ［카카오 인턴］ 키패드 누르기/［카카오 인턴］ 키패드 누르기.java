class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuffer res = new StringBuffer();
        // 우선 0을 10으로 11로 바꾸기
        for (int i=0; i<numbers.length; i++){
            if (numbers[i] == 0){
                numbers[i] = 11;
            }
        }
        
        // 시작
        int leftNumber = 10;
        int rightNumber = 12;
        for (int i=0; i<numbers.length; i++){
            //1, 4, 7
            if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7){
                leftNumber = numbers[i];
                res.append("L");
            }
            
            // 3, 6, 9
            else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9){
                rightNumber = numbers[i];
                res.append("R");
            }
            
            // 2, 5, 8, 10
            else{
                int leftDistance = getDistanceBetweenTwoNumber(leftNumber, numbers[i]);
                int rightDistance = getDistanceBetweenTwoNumber(rightNumber, numbers[i]);
                if (leftDistance < rightDistance){
                    leftNumber = numbers[i];
                    res.append("L");
                } else if (rightDistance < leftDistance){
                    rightNumber = numbers[i];
                    res.append("R");
                } else{
                    if (hand.equals("left")){
                        leftNumber = numbers[i];
                        res.append("L");
                    }
                    else {
                        rightNumber = numbers[i];
                        res.append("R");
                    }
                }
            }
            
        }
        return res.toString();
    }
    
    private int getDistanceBetweenTwoNumber(int firstNumber, int secondNumber){
        int firstRow = (firstNumber-1)/3;
        int firstColumn = (firstNumber-1)%3;
        int secondRow = (secondNumber-1)/3;
        int secondColumn = (secondNumber-1)%3;
        return Math.abs(firstRow-secondRow) + Math.abs(firstColumn-secondColumn);
    }
}