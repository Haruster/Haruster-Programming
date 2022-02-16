public class Circle {

    int radius;

    String name;

    // 생성자 이름은 클래스 이름과 동일하다.
    public Circle() { // 매개 변수 없는 생성자

        radius = 1; name = ""; // 필드 초기화

    }

    // 생성자는 리턴 타입 없음
    public Circle(int r, String n) { // 매개 변수를 가진 생성자

        // 생성자는 radius와 name 필드 초기화
        radius = r; name = n; // 매개 변수로 필드 초기화

    }

    public double getArea() {

        return 3.14 * radius * radius;

    }

    public static void main(String[] args) {

        Circle pizza = new Circle(10, "자바피자"); // 객체 생성, 반지름을 10으로, 이름을 "자바피자"로 초기화

        double area = pizza.getArea();

        System.out.println(pizza.name + "의 면적은 " + area);

        Circle donut = new Circle(); // 객체 생성. 반지름을 1, 이름을 ""로 초기화

        donut.name = "도넛피자"; // 이름 변경

        area = donut.getArea(); 

        System.out.println(donut.name + "의 면적은 " + area);

    }

}