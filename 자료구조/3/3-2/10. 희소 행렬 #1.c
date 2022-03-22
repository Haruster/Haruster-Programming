typedef struct {

    int row;
    int col;
    int value;

} element;

typedef struct SparseMatrix {

    element data[MAX_TERMS];
    
    int rows; // 행의 개수
    int cols; // 열의 개수
    int terms; // 항의 개수

} SparseMatrix;

Sparse Matrix matrix_transpose(SparseMatrix a) {


    SparseMatrix b;

    int bindex; // 행렬 b에서 현재 저장 위치

    b.rows = a.rows;
    b.cols = a.cols;
    b.terms = a.terms;

    if (a.terms > 0) {

        bindex = 0;

        for (int c = 0; c < a.cols; c++) {

            for (int i = 0; i < a.terms; i++) {

                if (a.data[i].col == c) {

                    b.data[bindex].row = a.data[i].col;
                    b.data[bindex].col = a.data[i].row;
                    b.data[bindex].value = a.data[i].value;

                    bindex++;

                }

            }

        }

    } 

    return b;

}

void matrix_print(SparseMatrix a) {

    printf("============================\n");

    for (int i = 0; i < a.terms; i++) {

        printf("(%d %d %d)\n", a.data[i].row, a.data[i].col, a.data[i].value);

    }

    printf("================================\n");

}

int main(void) {

    SparseMatrix m = {

        {{0, 3, 7}, {1, 0, 9}, {1, 5, 8}, {3, 0, 6}, {3, 1, 5}, {4, 5, 1}, {5, 2, 2}},
        6, 
        6, 
        7

    };

    SparseMatrix result;

    result = matrix_transpose2(m);
    matrix _print(result);
    return 0;

}