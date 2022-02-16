#include <stdio.h>

int main(void) {

    char *pc, c = 'A';

    int *pi, i = &i;

    printf("&c = %X, pc = %X, c = %5c, *pc = %5c\n", &c, pc, c, *pc);
    printf("&i = %X, pi = %X, i = %5d, *pi = %5d\n", &i, pi, i, *pi);

    (*pi)++; (*pc++);

    printf("i = %3d, c = %c\n", i, c);

    *pi += 1; *pc += 1;

    printf("i = %3d, c = %c\n", i, c);

    (*pi) += 1; (*pc) += 1;

    printf("i = %3d, c = %c\n", i, c);

    ++*pi; ++*pc;

    printf("i = %3d, c = %c\n", i, c);

    ++(*pi); ++(*pc);

    printf("i = %3d, c = %c\n", i, c);

    *pi++; *pc++;

    printf("&c = %X, pc = %X, c= %5c, *pc = %5c\n", &c, pc, c, *pc);
    printf("&i = %X, pi = %X, i = %5d, *pi = %5d\n", &i, pi, i, *pi);

    return 0;

}