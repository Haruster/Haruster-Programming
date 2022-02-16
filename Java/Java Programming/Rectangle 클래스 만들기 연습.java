import java.util.Scanner;

class Rectangle {

    int width; // 너비 필드
    int height; // 높이 필드

    public int getArea() {

        return width * height; // 너비와 높이 필드를 곱한 값을 반환한다.

    }

}

public class main {

    public static void main(String[] args) {

        Rectangle rect = new Rectangle(); // 객체 생성

        Scanner scanner = new Scanner(System.in);

        System.out.print(">> ");

        rect.width = scanner.nextInt();
        rect.height = scanner.nextInt();

        System.out.println("사각형의 면적은 " + rect.getArea());

        scanner.close();

    }

}