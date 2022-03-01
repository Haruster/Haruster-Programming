#include <stdio.h>

int add(int a, int b);

int main(void) {

    int (*fpt)(int a, int b);
    int a, b, sum;

    a = 10;
    b = 20;

    fpt = add; // add 함수의 시작 주소를 할당한다.
    sum = fpt(a, b); // 함수 포인터 fpt를 이용해 add()를 호출한다.

    printf("sum = %d\n", sum);

    return 0;

}

// add() 함수 정의

int add(int a, int b) {

    return a + b;

}