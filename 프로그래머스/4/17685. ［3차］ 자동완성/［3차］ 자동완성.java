class Solution {
    TrieNode root;
    public int solution(String[] words) {
        root = new TrieNode();
        for (String word: words){
            insertNode(word);
        }
        int res = 0;
        for (String word: words){
            res += getMinCount(word);
        }
        return res;
    }
    
    private int getMinCount(String verb){
        int minCnt = 0;
        TrieNode node = root;
        for (int i=0; i<verb.length(); i++){
            minCnt++;
            char character = verb.charAt(i);
            int idx = (int)(character-'a');
			if (node.nodeCounts[idx] == 1){
                return minCnt;
            }
            node = node.nextNodes[idx];
        }
        return minCnt;
    }
    
    private void insertNode(String verb){
        TrieNode node = root;
        for (int i=0; i<verb.length(); i++){
            char character = verb.charAt(i);
            int idx = (int)(character-'a');
            // 비어 있으면 추가
            if (node.nextNodes[idx] == null){
                node.nextNodes[idx] = new TrieNode();
            }
            node.nodeCounts[idx]++;
            node = node.nextNodes[idx];
        }
        node.isEnd = true;
    }
}

class TrieNode{
    boolean isEnd;
    TrieNode[] nextNodes;
    int[] nodeCounts;
    
    TrieNode(){
        nextNodes = new TrieNode[26];
        nodeCounts = new int[26];
        isEnd = false;
    }
}