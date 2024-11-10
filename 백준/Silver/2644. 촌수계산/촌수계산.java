import java.util.*;

public class Main {
    public static List<Integer>[] arr;
    public static void getShortestDistance(int n, int start, int end){
        // 큐
        Queue<int[]> queue = new LinkedList<>();

        // 방문 여부 배열
        Boolean[] isVisited = new Boolean[n+1];
        for (int i = 0; i<n+1; i++){
            isVisited[i] = false;
        }

        // 초기 값
        queue.add(new int[]{start, 0});
        isVisited[start] = true;

        // 순회
        while (!queue.isEmpty()){
            int[] tempArr = queue.remove();
            int currentNode = tempArr[0];
            int currentDistance = tempArr[1];
            // 찾았으면 끝
            if (currentNode == end){
                System.out.println(currentDistance);
                System.exit(0);
            }

            // 연결된 모든 노드 방문
            List<Integer> linkedList = arr[currentNode];
            for (int i = 0; i< linkedList.size(); i++){
                Integer nextNode = linkedList.get(i);
                // 방문하지 않았을 때
                if (!isVisited[nextNode]){
                    queue.add(new int[]{nextNode, currentDistance+1});
                    isVisited[nextNode] = true;
                }
            }
        }
        System.out.println(-1);
    }
    public static void main(String[] args) {
        // 스캐너
        Scanner sc = new Scanner(System.in);

        // 전체 사람 수
        int n = Integer.parseInt(sc.nextLine());

        // 촌수 계산 할 두 사람
        String str = sc.nextLine();
        StringTokenizer st = new StringTokenizer(str);
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        // 인접 리스트 생성
        arr = new ArrayList[n+1];
        for (int i = 1; i<=n; i++){
            arr[i] = new ArrayList<>();
        }

        // 엣지 추가
        int m = Integer.parseInt(sc.nextLine());
        for (int i = 0; i<m ;i++){
            st = new StringTokenizer(sc.nextLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr[x].add(y);
            arr[y].add(x);
        }

        getShortestDistance(n, a, b);
    }
}