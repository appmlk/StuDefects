import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner An = new Scanner(System.in);
        int N = An.nextInt();
        String S = An.nextLine();
        int M = S.indexOf("ABC");
        if (M == -1) {
            System.out.println(M);
        } else {
            System.out.println(M + 1);
        }
    }
}