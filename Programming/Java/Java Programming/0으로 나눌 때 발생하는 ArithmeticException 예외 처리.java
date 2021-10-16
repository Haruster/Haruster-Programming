import java.util.Scanner;

public class main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in); //사용자 값을 입력 받을 수 있는 scanner 선언

        while (true) {

            System.out.print("나뉨수를 입력하세요 : ");
            int dividend = scanner.nextInt(); // 나뉨수를 입력받는다.

            System.out.print("나눗수를 입력하세요 : ");
            int divisor = scanner.nextInt(); //나눗수를 입력받는다. 

            try {

                System.out.println(dividend + "를" + divisor + "로 나눈 몫은" + dividend/divisor + "입니다.");

                break; // 정상적인 나누기 완료 후에 while문 벗어나기

            }
            catch (ArithmeticException e) { // ArithmeticException 예외 처리 코드

                System.out.println("0으로 나눌 수 업습니다. !! 다시 입력하세요.");

            }
        }

        scanner.close();

    }

}