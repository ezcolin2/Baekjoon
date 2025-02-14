import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String firstString = br.readLine();
        String secondString = br.readLine();

        LCSInformation res = getLCSLength(firstString, secondString);

        bw.write(String.valueOf(res.LCSLength));
        if (res.LCSLength > 0) {
            bw.write("\n" + res.LCSString);
        }
        bw.close();
    }

    public static LCSInformation getLCSLength(String firstString, String secondString) {
        int firstStringLength = firstString.length();
        int secondStringLength = secondString.length();

        int[][] dp = new int[firstStringLength + 1][secondStringLength + 1];

        // LCS 길이 구하기
        for (int i = 1; i <= firstStringLength; i++) {
            for (int j = 1; j <= secondStringLength; j++) {
                if (firstString.charAt(i - 1) == secondString.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        // LCS 문자열 역추적 (Backtracking)
        StringBuilder LCSString = new StringBuilder();
        int i = firstStringLength, j = secondStringLength;

        while (i > 0 && j > 0) {
            if (firstString.charAt(i - 1) == secondString.charAt(j - 1)) {
                LCSString.append(firstString.charAt(i - 1));
                i--;
                j--;
            } else if (dp[i - 1][j] > dp[i][j - 1]) {
                i--;
            } else {
                j--;
            }
        }

        return new LCSInformation(dp[firstStringLength][secondStringLength], LCSString.reverse().toString());
    }

    public static class LCSInformation {
        int LCSLength;
        String LCSString;

        LCSInformation(int LCSLength, String LCSString) {
            this.LCSLength = LCSLength;
            this.LCSString = LCSString;
        }
    }
}
