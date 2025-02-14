import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] possibleWeights = getAllPossibleWeights(n);
        if (possibleWeights.length == 0){
            bw.write(String.valueOf(-1));
        }
        for (int i:possibleWeights){
            bw.write(String.valueOf(i));
            bw.write('\n');
        }
        bw.close();
    }

    /**
     * A^2 - B^2 = distance를 만족하는 모든 A 값을 구한다.
     * @param distance
     * @return
     */
    public static int[] getAllPossibleWeights(int distance){
        List<Integer> possibleWeights = new ArrayList<>();
        // two pinter를 사용한다.
        int previousWeight = 1;
        int currentWeight = 2;
        while (previousWeight<currentWeight){
            int currentDistance = currentWeight*currentWeight -previousWeight*previousWeight;
            if (currentDistance == distance){
                possibleWeights.add(currentWeight);
                currentWeight++;
                previousWeight++;
            }
            else if (currentDistance < distance){
                currentWeight++;
            } else{
                previousWeight++;
            }
        }
        return possibleWeights.stream().mapToInt(Integer::intValue).toArray();
    }
}