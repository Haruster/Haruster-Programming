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
// 이중 연결 리스트의 노드를 출력한다.

void print_dlist(DListNode* phead) {

    DListNode* p;

    for (p = phead->rlink; p != phead; p = p->rlink) {

        printf("<-||%d|->", p->data);

    }

    printf("\n");

}

// 새로운 데이터를 노드 before의 오른쪽에 삽입한다.

void dinsert(DListNode *before, element data) {

    DListNode *newnode = (DListNode *)malloc(sizeof(DListNode));

    strcpy(newnode->data, data);

    newnode->llink = before;
    newnode->rlink = before->rlink;

    before->rlink->llink = newnode;
    before->rlink = newnode;

}

void ddlete(DListNode* head, DListNode* removed) {

        if (removed == head) return;

        removed->llink->rlink = removed->rlink;
        removed->rlink->llink = removed->llink;

        free(removed);

}


// 이중 연결 리스트 테스트 프로그램

int main(void) {

    DListNode* head = (DListNode *) malloc(sizeof(DListNode));

    init(head);

    printf("추가 단계");

    for (int i = 0; i < 5; i++) {

        // 헤드 노드의 오른쪽에 삽입

        dinsert(head, i);

        print_dlist(head);

    }

    printf("\n 삭제 단계 \n");

    for (int i = 0; i < 5; i++) {

        print_dlist(head);

        ddelete(head, head->rlink);

    } 

    free(head);

    return 0;

}
