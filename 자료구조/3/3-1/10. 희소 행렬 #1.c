typedef struct {

    int row;
    int col;
    int value;

} element;

typedef struct SparceMatrix {

    element data[MAX_TERMS];
    
    int rows; // 행의 개수
    int cols; // 열의 개수
    int terms; // 항의 개수

} SparceMatrix;