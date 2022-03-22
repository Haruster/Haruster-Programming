// 반복적 피보나치

#include <stdio.h>
#include <time.h>

int main(void) {

    int n;

    time_t start, end;

    start = clock(); // 수행 시간 측정 시작

    if (n == 0) return 0;
    if (n == 1) return 1;

    int pp = 0; // 전전수
    int p = 1; // 전수
    int result = 0;

    for (int i = 2; i <= n; i++) {

        result = p + pp;

        pp = p;

        p = result;

    }

    end = clock();

    double tresult = (double)(end - start);

    printf("%f", tresult);

}
