#include <stdio.h>
#include <time.h>

int main(void) {

    int i, j, mul;
    int n = 1000;

    mul = 1;

    time_t start, end;

    start = clock(); // 수행 시간 측정 시작

    for (i = 0; i < n; i++) {

        for (j = 1; j < n; j++) {

            mul = mul * j;

        }

    }
    end = clock(); // 시간 측정 끝

    double result = (double)(end - start);

    printf("%f", result);

}