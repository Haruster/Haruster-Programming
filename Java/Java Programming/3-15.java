import java.util.Scanner;

public class main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {

            System.out.print("나뉨수를 입력하시오 : ");
            int diviend = scanner.nextInt(); //나뉨수 입력

            System.out.print("나눗수를 입력하시오 : ");
            int divisor = scanner.nextInt(); //나눗수 입력

            try {

                System.out.println(diviend + "를" + divisor + "로 나눈 값은" + diviend/divisor + "입니다.");

                break; //정상적인 나누기 완료 후 while문을 벗어나기

            }
            catch (ArithmeticException e){ // ArithmeticException

                System.out.println("0으로 나눌 수 없습니다.! 다시 입력해주세요");

            }

        }

        scanner.close();

    }
}