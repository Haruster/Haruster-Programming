#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK_SIZE 100

// 프로그램 4.3에서 스택 코드 추가

typedef char element;   // 교체!

// ...

// 프로그램 4.3에서 스택 코드 추가 끝

// 연산자의 우선 순위를 반환한다.

int prec(char op) {

    switch (op) {

        case '(': case ')': return 0;

        case '+': case '-': return 1;

        case '*': case '/': return 2:

    }

    return -1;

}

// 중위 표기 수식 -> 후위 표기 수식

void infix_to_postfix(char exp[]) {

    int i = 0;

    char ch, top_op;

    int len = strlen(exp);

    StackType s;

    init_stack(&s); // 스택 초기화

    for (i = 0; i < len; i++) {

        ch = exp[i];

        switch (ch) {

            case '+': case '-': case '*': case '/': // 연산자

            // 스택에 있는 연산자의 우선 순위가 더 크거나 같으면 출력한다.

                while(!is_empty(&s) && (prec(ch)) <= prec(peek(&s)))

                    printf("%c", pop(&s));

                push(&s, ch);

                break;
            
            case '(': // 왼쪽 괄호

                push(&s, ch);

                // 왼쪽 괄호를 만날 때까지 출력
                while (top_op != '(') {

                    printf("%c", top_op);

                    top_op = pop(&s);

                }

                break;

            default:

                printf("%c", ch);

                break;

        }

    }

    while (!is_empty(&s)) // 스택에 저장된 연산자들 출력

        printf("%c", pop(&s));

}

// main 함수

int main(void) {

    char *s = "(2+3)*4+9";

    printf("중위표시수식 %s\n", s);
    printf("후휘표시수식 ");

    infix_to_postfix(s);

    printf("\n");

    return 0;

}