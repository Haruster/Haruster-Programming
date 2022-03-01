#include <stdio.h>

int add(int a, int b);
int sub(int a, int b);
int mul(int a, int b);
int div(int a, int b);

int main(void) {

    int(*fpt[4])(int a, int b); // 함수 포인터 배열 선언
    int a, b, res, num;

    fpt[0] = add;
    fpt[1] = sub;
    fpt[2] = mul;
    fpt[3] = div;

    do {

        printf("1. add, 2. sub, 3. mul, 4. div, 5.exit : ");
        
        scanf("%d", &num);

        if (num == 5) break;

        printf("\nInput Number for a, b : \n");

        scanf("%d %d", &a, &b);

        res = fpt[num - 1](a, b);

        printf("result = %d\n", res);

    } while(1);

    return 0;

}

int add(int a, int b) {

    return a + b;

}

int sub(int a, int b) {

    return a - b;

}

int mul(int a, int b) {

    return a * b;

}

int div(int a, int b) {

    return a / b;

}