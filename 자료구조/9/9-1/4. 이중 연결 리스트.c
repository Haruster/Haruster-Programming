// 이중 연결 리스트 테스트 프로그램

#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct DListNode { // 이중 연결 노드 타입

    element data;

    struct DListNode* llink;
    struct DListNode* rlink;

} DListNode;

// 이중 연결 리스트를 초기화한다.

void init(DListNode* phead) {

    phead->llink = phead;
    phead->rlink = phead;

}