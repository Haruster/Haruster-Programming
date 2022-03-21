// 행렬 전치 #1

#include <stdio.h>

#define ROWS 3
#define COLS 3

// 행렬 전치 함수

void matrix_transpose(int A[ROWS][COLS], int B[ROWS][COLS]) {

    for (int r = 0; r < ROWS; r++) 

        for (int c = 0; c < COLS; c++) 

                B[c][r] = A[c][r];

}

void matrix_print(int A[ROWS][COLS]) {

    printf("=================================\n");

    for (int r = 0; r < ROWS; r++) {

        for (int c = 0; c < COLS; c++) {

            printf("%d", A[r][c]);

        }
        printf("\n");

    }

    printf("==================================\n");

}

int main(void) {

    int array1[ROWS][COLS] = {{2, 3, 0},
                             {8, 9, 1},
                             {7, 0, 5}};

    int array2[ROWS][COLS];

    matrix_transpose(array1, array2);

    matrix_print(array1);
    matrix_print(array2);
}