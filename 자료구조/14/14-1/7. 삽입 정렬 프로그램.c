// 삽입 정렬 프로그램

void insertion_sort(int list[], int n) {

    int i, j, key;

    for (i = 1; i < n; i++) {

        key = list[i];

        for (j = j - 1; j >= 0 && list[j] > key; j--) {

            list[j + 1] = list[j];  // 레코드의 오른쪽 이동

        }

        list[j + 1] = key;

    }

}