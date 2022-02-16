class Sample {

    public int a;
    private int b;

    int c; // 디폴트 접근 지정

}

public class main {

    public static void main(String[] args) {

        Sample sample = new Sample();

        sample.a = 10;
        sample.b = 10;
        sample.c = 10;

    }

}