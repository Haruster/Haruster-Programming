// 반복적 피보나치

#include <stdio.h>
#include <time.h>

int fib (int n) {

    if (n < 2) return n;

    else {

        int i, tmp, cur = 1, last = 0;

        for (i = 2; i <= n; i++) {

            tmp = cur;
            cur += last;
            last = tmp;

        }

        return cur;

    }
    

}

int main(void) {

    int n = 10;

    time_t start, end;

    start = clock(); // 수행 시간 측정 시작

    printf("%d", fib(n));

    end = clock();

    double tresult = (double)(end - start);

    printf("%f", tresult);

}
