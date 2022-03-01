#include <stdio.h>

int main(void) {

    int a[2][3] = {10, 20, 30, 40, 50, 60};
    int *p1, *p2, *p3, i, j;

    p1 = a;
    p2 = a[0];
    p3 = a[1];

    printf("a = %p, a[0] = %p, a[1] = %p\n", a, a[0], a[1]);
    printf("p1 = %p, p2 = %p, p3 = %p\n", p1, p2, p3);

    printf("\n");

    for(p1 = a, i = 0; i < 6; i++) 

        printf("p1 + %d = %p, *(p1 + %d) = %d\n", i, (p1 + i), i, *(p1 + i));

    printf("\n");

    for(i = 0; i < 2; i++) {

        for(j = 0; j < 3; j++) {

            printf("a[%d] = %p *(a + %d) = %p a[%d][%d] = %d *(a[%d] + %d) = %d *(*(a + %d) + %d) = %d\n", i, a[i], i, *(a + i), i, j, a[i][j], i, j, *(a[i] + j), i, j, *(*(a + i) +j));

        }

    }

    return 0;


}