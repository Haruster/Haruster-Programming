// 허프만 코드 프로그램

#include <stdio.h>
#include <stdlib.h>

#define MAX_ELEMENT 200

typedef struct TreeNode {

    int weight;

    char ch;

    struct TreeNode *left;
    struct TreeNode *right;

} TreeNode;

typedef struct {

    TreeNode* ptree;

    char ch;

    int key;

} element;

typedef struct {

    element heap[MAX_ELEMENT];

    int heap_size;

} HeapType;

// 생성 함수

HeapType* create() {

    return (HeapType*)malloc(sizeof(HeapType));

}

// 초기화 함수

void init(HeapType* h) {

    h->heap_size = 0;

}

// 현재 요소의 개수가 heap_size인 히프 h에 item을 삽입한다.

// 삽입 함수

void insert_min_heap(HeapType* h, element item) {

    

}
