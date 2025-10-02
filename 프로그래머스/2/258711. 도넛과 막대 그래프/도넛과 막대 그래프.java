import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    private int MAX_LENGTH = 1_000_000;
    private List<List<Integer>> graph;
    private List<List<Integer>> reverseGraph;
    private boolean[] totalVisited = new boolean[MAX_LENGTH+1];
    private boolean[] realVisited = new boolean[MAX_LENGTH+1];
    
    public int[] solution(int[][] edges) {
        int newNode = makeGraphAndFindNewNode(edges);
        return getGraphTypeCounts(newNode);
    }
    
    // 모든 그래프 종류의 개수를 구한다.
    private int[] getGraphTypeCounts(int newNode){
        int[] graphTypeCounts = new int[4];
        graphTypeCounts[0] = newNode;
        for (int i=1; i<=MAX_LENGTH; i++){
            // 새로 만들어진 정점은 스킵
            if (i == newNode){
                continue;
            }
            
            // 없으면 스킵
            if (graph.get(i).size()==0 && reverseGraph.get(i).size()==0){
                continue;
            }
            
            // 해당 노드의 그래프 타입을 구한다.
            int type = getGraphType(i);
            
            if (type==-1){
                continue;
            }
            
            // 막대의 경우 부모 노드를 찾아서 한 번 더 타입을 구해서 방문 처리한다.
            if (type == 2){
                int rootNode = getRootNode(i, newNode);
                getGraphType(rootNode);
            }
            
            graphTypeCounts[type]++;
        }
        
        return graphTypeCounts;
    }
    
    // 노드의 루트 노드를 구한다.
    private int getRootNode(int node, int newNode){
        // 부모 노드가 없을 때까지
        while (reverseGraph.get(node).size() > 0){
            if (reverseGraph.get(node).get(0) == newNode){
                // 새로운 노드인데 길이가 1이라면
                if (reverseGraph.get(node).size() == 1){
                    return node;
                }
                node = reverseGraph.get(node).get(1);
                
            } else{
                node = reverseGraph.get(node).get(0);
            }
        }
        return node;
    }
    
    private int makeGraphAndFindNewNode(int[][] edges){
        graph = new ArrayList();
        reverseGraph = new ArrayList();
        for (int i=0; i<=MAX_LENGTH; i++){
            graph.add(new ArrayList());
            reverseGraph.add(new ArrayList());
            
        }
        
        // 모든 간선을 확인하면서 각 노드를 향하는 간선의 개수를 구한다.
        int[] fromEdgeCounts = new int[MAX_LENGTH+1];
        for (int[] edge: edges){
            graph.get(edge[0]).add(edge[1]);
            reverseGraph.get(edge[1]).add(edge[0]);
            fromEdgeCounts[edge[1]]++;
        }
        
        // 모든 노드를 확인하면서 각 노드를 향하는 간선의 개수가 0이면서 다른 노드로 향하는 간선이 2 이상인 노드를 구한다.
        int newNode = -1;
        for (int i=1; i<=MAX_LENGTH; i++){
            if (fromEdgeCounts[i] == 0 && graph.get(i).size()>=2){
                newNode = i;
            }
        }
        
        return newNode;
    }   
    
    // 특정 노드를 포함하고 있는 그래프의 타입을 구한다.
    private int getGraphType(int startNode){
        if (totalVisited[startNode]){
            return -1;
        }
        // type 1: 도넛, type 2: 막대, type 3: 8자
        int type = 1;
        
        // 초기 값 넣기 
        Queue<Integer> queue = new LinkedList();
        queue.add(startNode);
        totalVisited[startNode] = true;
        
        // BFS 시작
        while (!queue.isEmpty()){
            int node = queue.remove();
            
            // 다른 노드로 향하는 간선이 2개 이상이라면 8자 모양
            if (graph.get(node).size() >= 2){
                type = 3;
            }
            
            // 다른 노드로 향하는 간선이 없다면 막대
            if (graph.get(node).size() == 0){
                type = 2;
            }
            
            // 연결된 노드 방문
            for (int nextNode: graph.get(node)){
                if (totalVisited[nextNode]){
                    continue;
                }
                
                // 방문하지 않았다면 방문
                queue.add(nextNode);
                totalVisited[nextNode] = true;
            }
        }
        return type;
    }
}