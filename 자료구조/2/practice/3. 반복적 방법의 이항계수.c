#include <stdio.h>

int Factorial(int N) {

    if(N == 0) {

        return 1;

    }

    int i;
    int result = 1;

    for (i = N; i >= 1; i--) {

        result *= i;

    }

    return result;

} 

int main(void) {

    int n;
    int k;
    int result;

    print("n과 k값을 입력해주세요 : ");
    scanf("%d %d", &n, &k);

    result = Factorial(n) / (Factorial(k) * Factorial(n * k));

    printf("%dC%d = %d\n", n, k, result);

    return 0;

}