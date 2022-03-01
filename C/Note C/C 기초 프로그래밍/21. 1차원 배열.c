#include <stdio.h>

int main(void) {

    int Array1[5] = {1, 2, 3, 4, 5};

    for(int i = 0; i < 5; i++) {

        printf("Array1[%d]의 값은 %d입니다.\n", i, Array1[i]);

    }

    return 0;

}