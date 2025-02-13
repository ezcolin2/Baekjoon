import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Map;
import java.util.HashMap;

/**
 * 연속해서 먹는 접시의 수의 범위를 정한다.
 * 이 범위 내부에서 각 초밥 별 등장한 횟수를 저장한다.
 * two pointer를 통해 양쪽 끝을 이동하면서 왼쪽에 있는 초밥은 제거하고 오른쪽에 존재하는 초밥은 추가한다.
 * 시간 복잡도를 줄이기 위해 HashMap을 사용한다.
 * 만약 key가 존재하지 않으면 0으로 세팅해서 생성하고 0이 되면 해당 key를 삭제한다.
 */

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        for (int i=0; i<n; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        bw.write(String.valueOf(getMaxNumberOfKinds(arr, d, k, c)));
        bw.close();

    }

    public static int getMaxNumberOfKinds(int[] arr, int totalNumberOfKinds, int consecutiveNumber, int couponNumber){
        int n = arr.length;
        Map<Integer, Integer> map = new HashMap<>();

        // two pointer
        int left=0;
        int right=0;

        // 우선 연속해서 초밥을 먹어서 초기 값을 세팅한다.
        for (int i=0; i<consecutiveNumber-1; i++){
            // key가 없다면 1로 생성
            if (!map.containsKey(arr[right])){
                map.put(arr[right], 1);
            }

            // key가 있다면 증가
            else{
                int originValue = map.get(arr[right]);
                map.put(arr[right], originValue+1);
            }
            right++;
            right%=n;
        }
        // key가 없다면 1로 생성
        if (!map.containsKey(arr[right])){
            map.put(arr[right], 1);
        }

        // key가 있다면 증가
        else{
            int originValue = map.get(arr[right]);
            map.put(arr[right], originValue+1);
        }
        // 현재 범위에서 초밥의 가짓수를 구한다.
        int res;
        // 쿠폰 번호가 있으면 그냥 key 개수
        if (map.containsKey(couponNumber)){
            res = map.size();
        }
        // 없으면 key 개수 + 1;
        else{
            res = map.size()+1;
        }
        left++;
        right++;
        left%=n;
        right%=n;

        // 지금부터 two pointer 탐색을 시작한다.
        for (int i=0; i<n-1; i++){
            // left를 뺀다.
            // 하나 남았다면 제거한다.
            if (map.get(arr[left-1])==1){
                map.remove(arr[left-1]);
            }
            // 더 남았다면 개수를 줄인다.
            else{
                int originNumber = map.get(arr[left-1]);
                map.put(arr[left-1], originNumber-1);
            }

            // right를 더한다.
            // key가 없다면 1로 생성
            if (!map.containsKey(arr[right])){
                map.put(arr[right], 1);
            }

            // key가 있다면 증가
            else{
                int originValue = map.get(arr[right]);
                map.put(arr[right], originValue+1);
            }

            // 쿠폰 번호가 있으면 그냥 key 개수
            if (map.containsKey(couponNumber)){
                res = Math.max(res, map.size());
            }
            // 없으면 key 개수 + 1;
            else{
                res = Math.max(res, map.size()+1);
            }
            left++;
            right++;
            left%=n;
            right%=n;
        }
        return res;
    }
}