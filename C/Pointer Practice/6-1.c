#include <stdio.h>

int main(void) {

    char *pc, c = 'A';
    int *pi, i = 129;
    float *pf, f = 10.23;
    double *pd, d = 12.35;

    pc = &c; // c의 번지를 pc에 대입한다.
    pi = &i; // i의 번지를 pi에 대입한다.
    pf = &f; // f의 번지를 pf에 대입한다.
    pd = &d; // d의 번지를 pd에 대입한다.

    printf("&c = %x, pc = %x, c = %5c, *pc = %5c\n", &c, pc , c, *pc);
    printf("&i = %x, pi = %x, i = %5d, *pi = %5d\n", &i, pi, i, *pi);
    printf("&f = %x, pf = %x, f = %3.2f, *pf = %3.2f\n", &f, pf, f, *pf);
    printf("&d = %x, pd = %x, d = %3.2f, *pd = %3.2f \n", &d, pd, d, *pd);

    printf("sizeof(pc) = %d\n", sizeof(pc));
    printf("sizeof(pi) = %d\n", sizeof(pi));
    printf("sizeof(pf) = %d\n", sizeof(pf));
    printf("sizeof(pd) = %d\n", sizeof(pd));

    return 0;


}