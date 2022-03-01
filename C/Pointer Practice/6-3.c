#include <stdio.h>

int main(void) {

    char a[] = "Hello";

    int n[5] = {10, 20, 30, 40, 50};

    char *p1, *p2;
    int *p3, i;

    p1 = a;
    p2 = &a[2];
    p3 = n;

    printf("a = %p, p1 = %p, p2 = %p\n", a, p1, p2);
    printf("n = %p, p3 = %p\n", n, p3);

    printf("\np1 --> ");

    for(i = 0; i< 5; i++, p1++) 

printf("%c", *p1);

    

    printf("\np2 --> ");

    for(; *p2 != NULL; p2++) 

        printf("%c", *p2);

    

    printf("\np3 --> ");

    for(i = 0; i < 5; i++, p3++) 

        printf("%d ", *p3);

    printf("\n\n");

    for(p3 = n, i = 0; i < 5; i++)

        printf("p3 + %d = %p, *(p3 + %d) = %d\n", i, (p3 + i), i, *(p3 + i));

    return 0;

    

}