// 1부터 100까지의 합을 구하는 프로그램

public class main {

    public static void main(String[] args) {

        int i;
        
        int sum = 0;

        for (i = 1; i <= 100; i++) {

            sum = sum + i;

            System.out.println("sum(0~"+i+")"+sum);

        }

        System.out.println("Last Result : sum(100) = "+sum);

    }

}