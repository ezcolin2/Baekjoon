import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
    	Map<String, Integer> totalParkingMinutesMap = getTotalParkingMinutes(records);
		String[] sortedKeyArr = new String[totalParkingMinutesMap.size()];
        int i=0;
        for (String key: totalParkingMinutesMap.keySet()){
            sortedKeyArr[i++] = key;
        }
        Arrays.sort(sortedKeyArr, (a, b)->a.compareTo(b));

        
        int[] answer = new int[sortedKeyArr.length];
        for (int k=0; k<sortedKeyArr.length; k++){
            answer[k] = fees[1] + (int)(Math.ceil(Math.max(0, totalParkingMinutesMap.get(sortedKeyArr[k])-fees[0])/(double)(fees[2]))*fees[3]);
        }
        
        return answer;
    }
    
    private Map<String, Integer> getTotalParkingMinutes(String[] records){
    	Map<String, Integer> totalParkingMinutesMap = new HashMap();
    	Map<String, Integer> enteredMinutesMap = new HashMap();
        for (String record: records){
            String[] recordInfos = record.split(" ");
            String time = recordInfos[0];
            String carNumber = recordInfos[1];
            String type = recordInfos[2];
            
            // 들어왔다면
            if (type.equals("IN")){
                // 시간을 분으로 계산
                String[] timeInfos = time.split(":");
                int minutes = convertTimeToMinutes(time);
                enteredMinutesMap.put(carNumber, minutes);
            }
            
            // 나갔다면
            else{
                // 시간을 분으로 계산
                int leavedMinutes = convertTimeToMinutes(time);
                
                // 총 주차 시간 계산해서 삽입
                int enteredMinutes = enteredMinutesMap.get(carNumber);
                
                // 없으면 새로 삽입
                if (!totalParkingMinutesMap.containsKey(carNumber)){
                    totalParkingMinutesMap.put(carNumber, leavedMinutes - enteredMinutes);
                }
                
                // 있으면 추가
                else{
                    int originMinutes =totalParkingMinutesMap.get(carNumber);
                    totalParkingMinutesMap.put(carNumber, originMinutes + leavedMinutes - enteredMinutes);
                }
                enteredMinutesMap.remove(carNumber);
            }
        }
        
        // 아직도 안 나간 차량이 있다면 23:59로 일괄 계산
        for (Map.Entry<String, Integer> entry: enteredMinutesMap.entrySet()){
            String carNumber = entry.getKey();
            int enteredMinutes = entry.getValue();
            int leavedMinutes = convertTimeToMinutes("23:59");
            // 없으면 새로 삽입
            if (!totalParkingMinutesMap.containsKey(carNumber)){
                totalParkingMinutesMap.put(carNumber, leavedMinutes - enteredMinutes);
            }

            // 있으면 추가
            else{
                int originMinutes =totalParkingMinutesMap.get(carNumber);
                totalParkingMinutesMap.put(carNumber, originMinutes + leavedMinutes - enteredMinutes);
            }
        }
        return totalParkingMinutesMap;
    }
    
    private int convertTimeToMinutes(String time){
        String[] timeInfos = time.split(":");
        return Integer.parseInt(timeInfos[0])*60 + Integer.parseInt(timeInfos[1]);
    }
}