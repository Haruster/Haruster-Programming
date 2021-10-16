import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("수를 입력하시오 : ");

        int number = scanner.nextInt(); //정수를 입력받는다.

        if (number % 3 == 0) // 3으로 나눈 나머지가 0인지 검사

            System.out.println("3의 배수입니다.");

        else

            System.out.println("3의 배수가 아닙니다.");

        scanner.close();

    }
}