#include <stdio.h>

int main(void) {

    int one, two;
    int three, four, five;
    int six;

    scanf("%d %d", &one, &two);

    three = (one * ((two % 100) % 10));
    four = (one * ((two % 100) / 10));
    five = (one * (two / 100));
    
    six = one * two;
    
    printf("%d\n", three);
    printf("%d\n", four);
    printf("%d\n", five);
    
    printf("%d\n", six);
    
    return 0;


}
