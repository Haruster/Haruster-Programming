class Point {

    private int x, y; // 한 점을 구성하는 x, y 좌표

    public void set(int x, int y) {

        this.x = x; this.y = y;

    }

    public void showPoint() { // 점의 좌표 출력

        System.out.println("(" + x + "," + y + ")");

    }

}

class ColorPoint extends Point {

    private String color; // 정의 색

    public void setColor(String color) {

        this.color = color;

    }

    public void showColorPoint() { // 컬러 정의 좌표 출력

        System.out.println(color);
        showPoint(); // point 클래스의 showPoint() 호출

    }

}

public class main {

    public static void main(String[] args) {

        Point p = new Point(); // Point 객체 생성

        p.set(1, 2); // Point 클래스의 set() 호출
        p.showPoint(); 

        ColorPoint cp = new ColorPoint(); // ColorPoint 객체 생성

        cp.set(3, 4); // Point 클래스의 set() 호출
        cp.setColor("red");
        cp.showColorPoint(); // 컬러와 좌표 출력

    }

}