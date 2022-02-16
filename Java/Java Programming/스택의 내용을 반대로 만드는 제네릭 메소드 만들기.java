// 스택의 내용을 반대로 만드는 제네릭 메소드 만들기

public class main {

    public static <T> GStack<T> reverse(GStack<T> a) { // T기 타입 매개변수인 제네릭 메소드
    
        GStack<T> s = new GStack<T>(); // 스택 a를 반대로 저장할 목적 GStack 생성

        while (true) {

            T tmp;

            tmp = a.pop(); // 원래 스택에서 요소 하나를 꺼냄

            if (tmp == null) // 스택이 비었음

                break;

            else 

                s.push(tmp); // 새 스택에 요소를 삽입

        }


        return s; // 새 스택을 리턴

    }

    public static void main(String[] args) {

        GStrack<Double> gs = new GStack<Double>(); // Double 타입의 GStack 생성

        for (int i = 0; i < 5; i++) { // 5개의 요소를 스택에 push 

            gs.push(new Double(i));

        }

        gs = reverse(gs);

        for (int i = 0; i < 5; i++) {

            System.out.println(gs.pop());

        }

    }

}