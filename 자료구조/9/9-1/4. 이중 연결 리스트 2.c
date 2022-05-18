// 이

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char element[100];
typedef struct DListNode {  // 이중 연결 노드 타입

    element data;

    struct DListNode* llink;
    struct DListNode* rlink;

} DListNode;

DListNode* current;

// 이중 연결 리스트를 초기화한다.

void init(DListNode* phead) {

    phead->llink = phead;
    phead->rlink = phead;

}

void ddlete(DListNode* head, DListNode* removed) {

    if (removed == head) return;

    removed->llink->rlink = removed->rlink;
    removed->rlink->llink = removed->llink;

    free(removed);

}

void dinsert(DListNode *before, element data) {

    DListNode *newnode = (DListNode *)malloc(sizeof(DListNode));

     strcpy(newnode->data, data);

    newnode->llink = before;
    newnode->rlink = before->rlink;

    before->rlink->llink = newnode;
    before->rlink = newnode;

}

// 이중 연결 리스트 테스트 프로그램

int main(void) {

    char ch;

    DListNode* head = (DListNode *)malloc(sizeof(DListNode));

    init(head);

    dinsert(head, "Mamamia");
    dinsert(head, "Dancing Queen");
    dinsert(head, "Fernando");

    current = head -> rlink;

    print_dlist(head);

    do {

        printf("\n 명령어를 입력하시오(<,>,q,): ");

        ch = getchar();

        if (ch == '<') {

            current = current->llink;

            if(current == head) {

                current = current->llink;

            }

            else if(ch == '>') {

                current = current -> rlink;

                if(current == head) {

                    current = current -> rlink;

                }

                print_dlist(head);

                getchar();

            } 

        } 
         
    } while (ch != 'q');

    // 동적 메모리 해제 코드를 여기에 넣기

}