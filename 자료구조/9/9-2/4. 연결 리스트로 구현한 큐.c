#include <stdio.h>
#include <stdlib.h>

typedef int element;    // 요소의 타입

typedef struct QueueNode {

    element data;

    struct QueueNode *link;

} QueueNode;

typedef struct { // 큐 ADT 구현
    
   QueueNode *front, *rear;
    
} LinkedQueueType;

// 삽입 함수

void enqueue(LinkedQueueType *q, element data) {

    QueueNode *temp = (QueueNode *)malloc(sizeof(QueueNode));

    temp->data = data;      // 데이터 저장
    temp->link = NULL;      // 링크 필드를 NULL

    if (is_empty(q)) {  // 큐가 공백이면
        
        q->front = temp;
        q->rear = temp;
        
    }

    else {  // 큐가 공백이 아니면

       q->rear->link = temp;   // 순서가 중요하다
        q->rear = temp;

    }

}

    // 삭제 함수

element dequeue(LinkedQueueType *q) {

    QueueNode *temp = q->front;

    element data;

   if (is_empty(q)) {  // 공백 상태

        fprintf(stderr, "스택이 비어 있음\n");

       exit(1);

    }

    else {

        data = temp->data;  // 데이터를 꺼낸다.

        q->front = q->front->link;  // front로 다음 노드

        if (q->front == NULL) {

            q->rear = NULL;

        }

        free(temp);     // 동적 메모리 해제

        return data;    // 데이터 반환

    }

}

