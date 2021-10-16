import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        int intArray[] = new int[5]; // 배열의 선언과 생성
        int sum = 0;

        Scanner scanner = new Scanner(System.in); 

        System.out.print(intArray.length + "개의 정수를 입력하세요 >>");

        for(int i = 0; i < intArray.length; i++) 
            intArray[i] = scanner.nextInt(); //키보드에서 입력받은 정수 저장

        for(int i = 0; i < intArray.length; i++) 
            sum += intArray[i]; //배열에 저장된 정수 값 더하기
        
        System.out.println("평균은 " + (double)sum / intArray.length);

        scanner.close();
    }

}