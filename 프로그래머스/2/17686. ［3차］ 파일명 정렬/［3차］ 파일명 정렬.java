import java.util.Comparator;
import java.util.Arrays;

class Solution {
    public String[] solution(String[] files) {
        File[] newFiles = new File[files.length];
        for (int i=0; i<files.length; i++){
            newFiles[i] = new File(files[i], i);
        }
        Comparator<File> comparator = (a, b)->{
            // head가 같다면 number 순
            if (a.head.equals(b.head)){
                // number도 같다면 들어온 순서
                if (a.number == b.number){
                    return a.sequence - b.sequence;
                }
                return a.number - b.number;
            }
            // 다르다면 head 순
            return a.head.compareTo(b.head);
        };
        Arrays.sort(newFiles, comparator);
        String[] answer = new String[files.length];
        for (int i=0; i<files.length; i++){
            answer[i] = newFiles[i].fileName;
        }
        return answer;
    }
}

class File{
    String fileName;
    String head;
    int number;
    String tail;
    int sequence;
    
    File(String fileName, int sequence){
        this.fileName = fileName;
        this.sequence = sequence;
        String lowerFileName = fileName.toLowerCase();
        int length = fileName.length();
        StringBuffer head = new StringBuffer();
        int idx = 0;
        // 숫자가 나올 때까지 반복
        while (idx<length && !Character.isDigit(lowerFileName.charAt(idx))){
            head.append(lowerFileName.charAt(idx++));
        }
        this.head = head.toString();
        // 숫자가 나왔다면 이제 숫자 구하기
        int number = 0;
        while(idx<length && Character.isDigit(lowerFileName.charAt(idx))){
            number*=10;
            number+=Integer.parseInt(String.valueOf(lowerFileName.charAt(idx++)));
        }
        this.number = number;
        // 문자가 나왔다면 나머지는 tail
        if (idx>=length){
            this.tail = "";
        }
        else{
            this.tail = lowerFileName.substring(idx, length);
        }
        
        System.out.print(head);
        System.out.print(" ");
        System.out.print(number);
        System.out.print(" ");
        System.out.print(tail);
        System.out.println();
    }
}