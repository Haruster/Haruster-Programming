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