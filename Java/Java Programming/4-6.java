class Circle {

    int radius;

    public Circle(int radius) {

        this.radius = radius;

    }

    public double getArea() {

        return 3.14 * radius * radius;

    }

    public static void main(String[] args) {

        Circle [] c; // Circle 배열에 대한 레퍼런스 c 선언

        c = new Circle[5]; // 5개의 레퍼런스 배열 생성


        for (int i = 0; i < c.length; i++) 
            c[i] = new Circle(i); // i 번째 원소 객체 생성


        for (int i = 0; i < c.length; i++)
            System.out.print((int)(c[i].getArea()) + " ");

    }

}