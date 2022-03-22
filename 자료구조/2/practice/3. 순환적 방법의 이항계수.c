#include <stdio.h>

int Factorial_NCK(int N, int K) {

    if(K == 1 || K == 0) {

        return 1;

    } else if ((0 < K) && (K < N)) {

        return Factorial_NCK(N - 1, K - 1) + Factorial_NCK(N - 1, K);

    } else {

        return 0;

    }

}

int main(void) {

    int n;
    int k;
    int result;

    print("n과 k값을 입력해주세요 : ");
    scanf("%d %d", &n, &k);

    result = Factorial_NCK(n, k);

    printf("%dC%d = %d\n", n, k, result);

    return 0;

}





