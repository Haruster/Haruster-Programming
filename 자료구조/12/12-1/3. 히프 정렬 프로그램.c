// 히프 정렬 프로그램

#include <stdio.h>
#include <stdlib.h>

#define SIZE 8

// .....

// 앞의 최대 히프 코드를 여기에 추가한다.

// .....

// 우선 순위 큐인 히프를 이용한 정렬

void heap_sort(element a[], int n) {

    int i;

    HeapType* h;

    h = create();

    init(h);

    for (i = 0; i < n; i++) {

        insert_max_heap(h, a[i]);

    }

    for (i = (n - 1); i >= 0; i--) {

        a[i] = delete_max_heap(h);

    }

    free(h);

}

int main(void) {

    element list[SIZE] = {23, 56, 11, 9, 56, 99, 27, 34};

    heap_sort(list, SIZE);

    for (int i = 0; i < SIZE; i++) {

        printf("%d", list[i].key);

    }

    printf("\n");

    return 0;

}