// 연결 리스트로 구현한 스택

#include <stdio.h>
#include <malloc.h>

typedef int element;
typedef struct StackNode {

    element data;

    struct StackNode *link;

} StackNode;

typedef struct {

    StackNode *top;

} LinkedStackType;

// 초기화 함수

void init(LinkedStackType *s) {

    s->top = NULL;

}

// 공백 상태 검출 함수

int is_empty(LinkedStackType *s) {

    return (s->top == NULL);

}

// 포화 상태 검출 함수

int is_full(LinkedStackType *s) {

    return 0;

}

// 삽입 함수

void push(LinkedStackType *s, element item) {

    StackNode *temp = (StackNode *)malloc(sizeof(StackNode));

    temp->data = item;
    temp->link = s->top;

    s->top = temp;

}

void print_stack(LinkedStackType *s) {

    for (StackNode *p = s->top; p != NULL; p = p->link) {

        printf("%d->", p->data);

    }

    printf("NULL \n");

}

// 삭제 함수

element pop(LinkedStackType *s) {

    if(is_empty(s)) {

        fprintf(stderr, "스택이 비어 있음\n");

        exit(1);

    }

    else {

        StackNode *temp = s->top;

        int data = temp->data;

        s->top = s->top->link;

        free(temp);

        return data;

    }

}

// 주 함수

int main(void) {

    LinkedStackType s;

    init(&s);

    push(&s, 1); print_stack(&s);
    push(&s, 2); print_stack(&s);
    push(&s, 3); print_stack(&s);

    pop(&s, 1); print_stack(&s);
    pop(&s, 2); print_stack(&s);
    pop(&s, 3); print_stack(&s);

    return 0;

}