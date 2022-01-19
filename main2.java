
public class main2 {
    public static void main(String[] args) {
        int ans = 0;
        int M = 0;
        int N = 0;
        for (int i=0;i<N;i++) {
            for (int j = i; j < N; j++) {
                int sum = 0;
                for(int k = i; k<=j;k++){
                sum += arr[k];
            }
            if (sum == M) {
                ans ++;
            }
        }
    }
}

// 구간을 찾아야함