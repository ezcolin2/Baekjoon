import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;

class Solution {
    public boolean solution(int n, int[][] path, int[][] order) {
    	ArrayList<Integer>[] graph = new ArrayList[n];
        for (int i=0; i<n; i++){
            graph[i] = new ArrayList();
        }
        for (int[] onePath: path){
        	graph[onePath[0]].add(onePath[1]);
        	graph[onePath[1]].add(onePath[0]);
        }
        ArrayList<Integer>[] orderGraph = makeOrderGraph(graph, order);
        return isGraphExist(orderGraph);
    }
    
    private boolean isGraphExist(ArrayList<Integer>[] graph){
        int n = graph.length;
        int[] inDegrees = new int[n];
        // 각 노드 별로 이 노드로 올 수 있는 노드의 개수를 구하기
        for (int i=0; i<n; i++){
            for (int nextNode: graph[i]){
                inDegrees[nextNode]++;
            }
        }
        
        // 사이클 판단 시작
        Queue<Integer> queue = new LinkedList();
        ArrayList<Integer> order = new ArrayList();
        queue.add(0);
        while(!queue.isEmpty()){
            int node = queue.remove();
            order.add(node);
            for (int nextNode: graph[node]){
                inDegrees[nextNode]--;
                if (inDegrees[nextNode]==0){
                    queue.add(nextNode);
                }
            }
        }
        
        return order.size() == n;
        
    }
    
    // order과 기존 그래프를 보고 순서 관계를 고려한 새로운 그래프를 생성한다.
    private ArrayList<Integer>[] makeOrderGraph(ArrayList<Integer>[] graph, int[][] order){
        int n = graph.length;
        Queue<Integer> queue = new LinkedList();
		ArrayList<Integer>[] orderGraph = new ArrayList[n];
        for (int i=0; i<n; i++){
            orderGraph[i] = new ArrayList();
        }
        boolean[] visited = new boolean[n];
        visited[0] = true;
        queue.add(0);
        while (!queue.isEmpty()){
            int node = queue.remove();
            for (int nextNode: graph[node]){
                if (!visited[nextNode]){
                    visited[nextNode] = true;
                    queue.add(nextNode);
                    orderGraph[node].add(nextNode);
                }
            }
        }
        for(int[] oneOrder: order){
            orderGraph[oneOrder[0]].add(oneOrder[1]);
        }
        return orderGraph;
    }
}