#include <stdio.h>

#define MAX_SIZE 100

typedef struct StackType {

    int stack[MAX_SIZE];
    int top;

} StackType;

void Stack_Init(StackType* s) {

    s->top = -1;

}

void Stack_Push(StackType* s, int item) {

    s->stack[++(s->top)] = item;

    return;

}

bool is_empty(StackType* s) {

    return s->top == -1;

}

int Stack_Pop(StackType* s) {

    int t = s->stack[s->top];
    
    s->stack[s->top] = 0;
    
    s->top--;

    return t;

}

int main(void) {

    StackType s;

    Stack_Init(&s);

    char input[MAX_SIZE] ={};

    printf("수식 : ");

    scanf("%s", input, sizeof(input));

    printf("괄호 수");

    int i = 0; 
    int count = 1;

    while (input[i] != NULL) {

        if(input[i] == '(') {

            Stack_Push(&s, count);

            printf("%d", count);

            count++;

        } else {

            printf("%d", Stack_Pop);

        }

        i++;

    }

    return 0;

}