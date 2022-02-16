// 1부터 100까지의 합을 구하는 프로그램

public class main {

    public static void main(String[] args) {

        int i;

        int sum = 0;

        for (i = 1; i <= 100; i++) {

            sum += i;

        }

        System.out.println("1부터 100까지의 합은 " + sum + "입니다.");

    }
}