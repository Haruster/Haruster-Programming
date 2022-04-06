#include <stdio.h>

#define ROWS 5
#define COLS 5

// 행렬 전치 함수

void matrix_transpose(int A[ROWS][COLS], int B[ROWS][COLS]) {

    for (int r = 0; r < ROWS; r++) {

        for (int c = 0; c < COLS; c++) {

            B[c][r] = A[r][c];

        }

    }

}

void matrix_print(int A[ROWS][COLS]) {

    printf("=============================\n");

    for (int r = 0; r < ROWS; r++) {

        for (int c = 0; c < COLS; c++) {

            printf("%d ", A[r][c]);


        }

        printf("\n");

    }

    printf("===============================\n");

}

int main(void) {

    int array1[COLS][ROWS] = {{1, 2, 5, 6, 7}, {1, 2, 3, 4, 5}, {5, 7, 4, 3, 2}, {4, 3, 2, 1, 1}, {1, 2, 3, 4, 5}};

    int array2[COLS][ROWS];

    matrix_transpose(array1, array2);
    
    matrix_print(array1);
    matrix_print(array2);
    
    return 0;

}
