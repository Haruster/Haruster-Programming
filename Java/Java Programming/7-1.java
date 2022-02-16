// 정수만 다루는 Vector<Integer> 컬렉션 활용

import java.util.Vector;

public class main {

    public static void main(String[] args) {

        Vector<Integer> v = new Vector<Integer>(); // 정수 값만 다루는 벡터 생성

        v.add(5); // 5삽입
        v.add(4); // 4삽입
        v.add(-1); // -1삽입

        // 벡터 중간에 삽입하기 
        v.add(2, 100); // 4와 -1사이에 정수 100 삽입

        System.out.println("벡터 내의 요소 객체 수 : " + v.size()); // 크기 3
        System.out.println("벡터의 현재 용량 : " + v.capacity()); // 벡터 용량 10

        // 모든 요소 정수 출력하기 
        for(int i = 0; i < v.size(); i++) {

            int n = v.get(i); // 벡터의 i 번째 정수
            
            System.out.println(n);

        }

        // 벡터 내의 모든 정수 더하기
        int sum = 0;

        for(int i = 0; i < v.size(); i++) {

            int n = v.elementAt(i); // 벡터의 i 번째 정수

            sum += n;

        }

        System.out.println("벡터에 있는 정수 합 : " + sum);

    }

}