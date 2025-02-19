import java.util.Set;
import java.util.HashSet;
class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        // 계산의 편의를 위해 1 줄인다.
        startday-=1;

        return getEmployeeCountForPrize(schedules, timelogs, startday);
        
    }
    
    /**
        늦었으면 true, 제대로 왔으면 false
        @param hopeTime : 출근 희망 시각
        @param realTime : 실제 출근 시각
    */
    private boolean isLate(String hopeTimeString, String realTimeString){
        
        // 만약 길이가 3이라면 앞에 0을 추가한다.
        if (hopeTimeString.length() == 3){
            hopeTimeString = "0"+hopeTimeString;
        }
        if (realTimeString.length() == 3){
            realTimeString = "0"+realTimeString;
        }
        
        // 분으로 변환한다.
        int hopeTimeMinute = Integer.parseInt(hopeTimeString.substring(0, 2))*60+Integer.parseInt(hopeTimeString.substring(2));
        int realTimeMinute = Integer.parseInt(realTimeString.substring(0, 2))*60+Integer.parseInt(realTimeString.substring(2));
        
        return realTimeMinute > hopeTimeMinute+10;
    }
    
    /**
        상품을 받게 될 직원 수를 반환한다.
    */
    private int getEmployeeCountForPrize(int[] schedules, int[][] timelogs, int startday){
        // 우선 집합에 모든 직원들을 넣는다.
        Set<Integer> set = new HashSet();
        for (int i=0; i<schedules.length; i++){
            set.add(i);
        }
        
        /**
            요일 별로 모든 직원들을 순회한다.
            1. 주말은 스킵한다.
            2. 평일에 지각한 직원은 바로 집합에서 제거한다.
            3. 끝까지 집합에 남아있는 직원들의 개수를 구한다.
        */
        for (int i=0; i<7; i++){
            // 현재 요일을 구한다.
            int currentDay = (startday+i)%7;
            
            // 주말은 스킵한다.
            if (currentDay == 5 || currentDay == 6){
                continue;
            }
            
            // 모든 직원들의 오늘 지각 여부를 구한다.
            for (int j=0; j<schedules.length; j++){
                // 평일에 지각하는 순간 바로 집합에서 제거한다.
                if (isLate(String.valueOf(schedules[j]), String.valueOf(timelogs[j][i]))){
                    set.remove(j);
                }
            }
        }
        return set.size();
    }
}