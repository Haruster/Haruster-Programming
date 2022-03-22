// 순환적 피보나치

#include <stdio.h>
#include <time.h>

int fib(int n) {

    if (n == 0) return 0;

    else if (n == 1) return 1;

    else return (fib(n - 1) + fib(n - 2));

}

int main(void) {

    time_t start, end;

    start = clock(); // 수행 시간 측정 시작

    int n = 10;
    int result;



    result = fib(n);

    end = clock();; // 시간 측정 끝

    double tresult = (double)(end - start);

    printf("%f", tresult);
}
