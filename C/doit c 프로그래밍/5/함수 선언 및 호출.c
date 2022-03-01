#include <stdio.h>

int Sum(int value1, int value2) {       // 사용자 정의 함수 Sum을 선언하고 매개변수로 value1과 value2를 선언한다.

    int result = value1 + value2;       // result = value1 + value2

    return result;      // result값을 반환한다.

}

void main() {

    int value = Sum(2, 3);      // value 변수에 2 + 3을 저장(Sum함수를 사용)

    printf("%d", value);        // value 변수를 출력

    return 0;

}