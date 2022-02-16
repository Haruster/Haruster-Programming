import java.util.Scanner;

public class main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int intArray[] = new int[5]; //배열 생성
        int max = 0; //현재 가장 큰 수

        System.out.println("양수 5개를 입력하세요.");

        for(int i = 0; i < 5; i++) {

            intArray[i] = scanner.nextInt(); //입력받은 정수를 배열에 저장함

            if(intArray[i] > max) // intArray[i]가 현재 가장 큰 수보다 크면
                max = intArray[i]; // intArray[i]를 max로 변경
        }
        System.out.println("가장 큰 수는 " + max + "입니다.");

        scanner.close();

    }

}