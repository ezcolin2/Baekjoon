import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    public static GasStation[] gasStations;
    public static Queue<Integer> priorityQueue;
    public static int getMinStopCount(int initialFuel){
        /**
         * 변수 1 : 현재 위치한 주유소
         * 변수 2 : 남아있는 연료 양
         * 변수 3 : 멈춘 횟수
         *
         * 현재 위치한 주유소와 멈춘 횟수가 같다면 남아있는 연료의 양이 가장 큰 것이 좋습니다.
         * 만약 현재 위치한 주유소에서 연료가 바닥났을 경우 지금까지 지나쳐 온 주유소에서 충전을 해야 합니다.
         * 당연히 지금까지 지나쳐 온 주유소 중 가장 연료르 많이 충전할 수 있는 곳에서 멈추는 것이 좋습니다.
         * 즉, 현재 위치에서 갈 수 있는 모든 주유소를 확인합니다.
         * 가장 멀리 갈 수 있는 주유소가 도착지가 아닐 경우 이전 주유소 중 한 곳에서 충전해야 합니다.
         * 그 중 가장 많이 충전할 수 있는 주유소에서 충전해야 합니다.
         *
         * 1. 현 시점에서 방문 가능한 모든 주유소의 연료들을 최대 힙에 넣는다.
         * 2. 최대 힙에서 꺼낼 때마다 방문 횟수를 증가시킨다.
         */
        int n = gasStations.length;
        int stopCount = 0;
        int fuel = initialFuel;

        // 현재 연료로 갈 수 있는 최대 주유소까지 들려서 모든 연료를 최대 힙에 넣는다.
        for (int i=0; i<n; i++){
            GasStation currentStation = gasStations[i];
            int currentLocation = currentStation.location;
            if (i>0){
                currentLocation -= gasStations[i-1].location;
            }
            int currentFuel = currentStation.fuelAmount;
            // 연료 소모
            fuel -= currentLocation;

            // 만약 연료가 남았으면
            if (fuel >= 0){
                priorityQueue.add(currentFuel);
                continue;
            }

            // 만약 연료가 다 떨어졌는데 최대 힙이 비었다면 끝
            if (priorityQueue.size() == 0){
                return -1;
            }

            // 연료가 다 떨어졌는데 최대 힙이 존재한다면 연료 보충
            else{
                while (fuel < 0){
                    if (priorityQueue.size() == 0){
                        return -1;
                    }
                    int tempFuel = priorityQueue.remove();
                    fuel += tempFuel;
                    stopCount += 1;

                }
                priorityQueue.add(currentFuel);
            }
        }

        return stopCount;
    }
    public static void main(String[] args) throws IOException{
        priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        // 주유소 배열
        gasStations = new GasStation[n+1];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            gasStations[i] = new GasStation(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }


        st = new StringTokenizer(br.readLine());
        int villageLocation = Integer.parseInt(st.nextToken());
        int initialFuel = Integer.parseInt(st.nextToken());
        gasStations[n] = new GasStation(villageLocation, 0);
        Arrays.sort(gasStations);
        System.out.println(getMinStopCount(initialFuel));

    }
    public static class GasStation implements Comparable<GasStation>{
        int location;
        int fuelAmount;
        GasStation(int location, int fuelAmount){
            this.location = location;
            this.fuelAmount = fuelAmount;
        }

        @Override
        public int compareTo(GasStation gasStation) {
            return Integer.compare(this.location, gasStation.location);
        }
    }
}